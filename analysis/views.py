from django.views.generic import View
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import DataFile

from pandas import DataFrame
import numpy as np

class HomeView(View):
    template_name = 'analysis/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.data_list(request))

    def data_list(self, request):
        dataList = DataFile.objects.all()
        data = []
        for each in dataList:
            data.append(each.dic())
        df = DataFrame(data)
        location_columns = df['location'].unique()
        sampleNo_columns = df['sampleNo'].unique()
        df = df.head(100)
        str_columns = ['date', 'week', 'group_blossoming', 'group_fruit', 'group_harvest', 'leaf_len', 'leaf_n',
                       'leaf_width', 'light', 'location', 'ped', 'plant_len', 'sampleNo', 'stem_width']
        df = df[str_columns]
        ko_columns = ['일자', '요일', '개화군', '착과군', '수확군', '잎길이(cm)', '잎수(개)', '잎폭(cm)', '수광량', '위치', 'PED', '경경(mm)', 'sampleNO', '초장(cm)']
        columns = np.asarray(ko_columns)
        dflist = np.asarray(df.values.tolist())
        return {'data_list' : dflist, 'columns':list(columns),
                'first_sam_op':sampleNo_columns[0], 'first_lo_op':location_columns[0],
                'location_columns':location_columns[1:], 'sampleNo_columns':sampleNo_columns[1:]}

class ClientView(View):
    template_name = 'analysis/client.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        dataList = DataFile.objects.all()
        data = []
        for each in dataList:
            data.append(each.dic())
        df = DataFrame(data)

        sampleNo = request.GET.get('sampleNo', None)
        location = request.GET.get('location', None)
        df = df[(df['sampleNo']==int(sampleNo)) & (df['location']==location)]
        data = {
            'labels': df['date'].tolist(),
            'leaf_len': df['leaf_len'].tolist(),
            'leaf_n': df['leaf_n'].tolist(),
            'leaf_width': df['leaf_width'].tolist(),
            'ped': df['ped'].tolist(),
            'plant_len': df['plant_len'].tolist(),
            'stem_width': df['stem_width'].tolist(),
        }
        return Response(data)

