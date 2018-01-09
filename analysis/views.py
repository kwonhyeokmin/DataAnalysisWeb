from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StandardDataFile, InvestigationData
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import os

class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

class HomeView(View):
    template_name = 'analysis/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.data_list(request))

    def data_list(self, request):
        # get 100 line from investigation data
        investigationDataList = InvestigationData.objects.all()[:100]
        investigationData = []
        for each in investigationDataList:
            investigationData.append(each.dic())

        df_investigationData = DataFrame(investigationData)
        str_columns = ['season', 'date', 'week', 'sampleNo', 'stem_width', 'plent_len', 'fcluster_n']
        df_investigationData = df_investigationData[str_columns]
        ko_columns = ['작기', '일자', '요일', 'sampleNo', '초장', '경경', '화방수']
        columns = np.asarray(ko_columns)
        df_investigationDataList = np.asarray(df_investigationData.values.tolist())

        investSampleData = InvestigationData.objects.values_list('sampleNo')
        investSampleList = []
        for each in investSampleData:
            investSampleList.append(int(each[0]))
        investSample = Series(investSampleList).unique()

        investSeasonData = InvestigationData.objects.values_list('season')
        investSeasonList = []
        for each in investSeasonData:
            investSeasonList.append(int(each[0]))
        investSeason = Series(investSeasonList).unique()

        model_files = os.listdir(UPLOAD_DIR)
        if len(model_files):
            first_model_file = model_files[0]
            data = {
                'data_list' : df_investigationDataList, 'columns':list(columns),
                'first_model_file':first_model_file,'model_files':model_files[1:],
                'model_samples':investSample[1:], 'first_model_sam':investSample[0],
                'seasons':investSeason[1:],'first_season':investSeason[0]
            }
            return data
        return {}

class InvestigateData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        sampleNo = request.GET.get('sampleNo', None)
        season = request.GET.get('season', None)

        dataList = InvestigationData.objects.all().filter(sampleNo=sampleNo, season=season)
        data = []
        for each in dataList:
            data.append(each.dic())
        df = DataFrame(data)

        if sampleNo!='undefined' or season!='undefined':
            data = {
                'labels': df['date'].tolist(),
                'leaf_len': df['stem_width'].tolist(),
                'leaf_n': df['plent_len'].tolist(),
                'leaf_width': df['fcluster_n'].tolist(),
            }
            return Response(data)
        else:
            return Response({})

class GrowthStageData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        target_file = request.GET.get('model', None)
        target_sample = request.GET.get('sampleNo', None)
        season = request.GET.get('season', None)

        if target_file != 'undefined' and target_sample != 'undefined' and season != 'undefined':
            filename = '{0}{1}'.format(UPLOAD_DIR, target_file)
            f = open(filename, 'rb')
            model = pickle.load(f)

            dataList = InvestigationData.objects.all().filter(season=season)
            target_sample = int(target_sample)
            data = []
            for each in dataList:
                data.append(each.dic())
            df = DataFrame(data)

            standard_day = df['date'][0]
            df['dataNo'] = df['date'].apply(lambda x: (x - standard_day).days + 1)

            sampleSize = len(df['sampleNo'].unique())
            samples = []
            for i in range(1, sampleSize+1):
                samples.append(df.loc[(df.sampleNo) == i])

            test_data = samples[target_sample]
            frame = DataFrame(test_data['dataNo'])
            frame = frame.reset_index(drop=True)

            test_data_table = pd.concat([frame, pd.DataFrame(model.predict(test_data[['stem_width', 'fcluster_n']]))], axis=1)
            predictX = [x for x in range(max(df['dataNo'])+1)]
            predictY = [x for x in range(max(df['dataNo'])+1)]

            count = 0
            prevNo = 0

            for dataNo in test_data_table['dataNo'].tolist():
                predictY[dataNo] = test_data_table[0].iloc[count]
                for i in range(prevNo, dataNo):
                    if count <= 0:
                        predictY[i] = 0
                    else:
                        predictY[i] = test_data_table[0].iloc[count-1]
                prevNo = dataNo
                count += 1
            data = {
                'predictX':predictX,
                'predictY':predictY
            }
            f.close()
            return Response(data)
        return Response({})

from sklearn import tree

UPLOAD_DIR = 'models/'   # models path
import pickle

@csrf_exempt
def model_update(request):
    if request.method == 'POST':
        dataList = StandardDataFile.objects.all()
        data = []
        for each in dataList:
            data.append(each.dic())
        df = DataFrame(data)

        standard_data = df[['id', 'plant_len_optimal', 'stem_optimal', 'fcluster_n']]
        standard_train = (standard_data[['plant_len_optimal', 'fcluster_n']]).values  ### 식물길이 / 줄기굵기
        standard_target = (df[['id']]).values  ### 일차

        clf = tree.DecisionTreeClassifier()
        model = clf.fit(standard_train, standard_target)

        # save the model to disk
        filename = '{0}{1}'.format(UPLOAD_DIR, 'DecisionTreeModel.sav')
        f = open(filename, 'wb')
        pickle.dump(model, f)
        f.close()

        return render(request, 'analysis/home_detail/growth_stage_chart.html', {})



