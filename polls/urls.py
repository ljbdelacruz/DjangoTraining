from django.conf.urls import url
from . import views
urlpatterns = [
    url('', views.index, name='index'),
    url('all', views.index, name='getall'),
]