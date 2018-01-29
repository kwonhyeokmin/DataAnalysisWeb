from django.conf.urls import url
from .views import HomeView, InvestigateData, IndexView, GrowthStageData, model_update

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^home/$', HomeView.as_view(), name="home"),
    url(r'^api/index/data', InvestigateData.as_view()),
    url(r'^api/growth/data', GrowthStageData.as_view()),
    url(r'^models/', model_update, name="models"),
]