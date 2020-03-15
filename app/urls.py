from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload_file, name='upload_file'),
    # path('info_form', views.request_page, name='info-form'),
    path('info_form', views.info_form, name='form'),
    url(r'^finish/$', views.finish, name='finish'),
]