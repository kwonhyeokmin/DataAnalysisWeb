from django.conf.urls import url
from .views import HomeView, ChartData

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^api/index/data', ChartData.as_view()),
]