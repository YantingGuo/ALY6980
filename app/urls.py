from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload_file, name='upload_file'),
    path('further_info', views.further_info, name='further_info')
]