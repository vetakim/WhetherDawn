from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.input, name='input'),
    url(r'^result/$', views.result, name='result'),
]