from django.conf.urls import url
from .views import HomeView, ChartData, ClientView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^client/$', ClientView.as_view(), name="client"),
    url(r'^api/index/data', ChartData.as_view()),
]