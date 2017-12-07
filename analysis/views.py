from django.views.generic import View
from django.shortcuts import render
from .models import DataFile
from pandas import DataFrame
import numpy as np
# Create your views here.
class HomeView(View):
    template_name = 'analysis/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.data_list(request))

    def data_list(self, request):
        dataList = DataFile.objects.all()
        data = []
        for each in dataList:
            data.append(each.dic())
        df = DataFrame(data).head(100)
        str_columns = ['date', 'week', 'group_blossoming', 'group_fruit', 'group_harvest', 'leaf_len', 'leaf_n',
                       'leaf_width', 'light', 'location', 'ped', 'plant_len', 'sampleNo', 'stem_width']
        df = df[str_columns]
        ko_columns = ['일자', '요일', '개화군', '착과군', '수확군', '잎길이(cm)', '잎수(개)', '잎폭(cm)', '수광량', '위치', 'PED', '경경(mm)', 'sampleNO', '초장(cm)']
        columns = np.asarray(ko_columns)
        dflist = np.asarray(df.values.tolist())
        return {'data_list' : dflist, 'columns':list(columns) }

class LineChart(View):
    template_name = 'analysis/linecharts.html'

    def get(self, request):
        dataList = DataFile.objects.all()
        data = []
        for each in dataList:
            data.append(each.dic())
        df = DataFrame(data)
        #print(df)
        columns = ['date', 'leaf_len']
        dataset = df[columns]
        return render(request, self.template_name, { 'Json' : dataset.to_json() })