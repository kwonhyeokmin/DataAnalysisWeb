from django.conf.urls import url
from .views import HomeView, LineChart

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^$', LineChart.as_view(), name="linecharts"),
]