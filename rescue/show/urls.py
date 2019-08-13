from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^drawing', views.drawing),
    url(r'^evacuation', views.evacuation)
]
