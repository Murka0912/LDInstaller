from django.urls import path

from .import views


urlpatterns = [
    path('',views.main, name= 'index'),
    path('upload', views.upload, name='upload'),
    path('ls',views.ls, name='ls'),
    path('files', views.file_list,name='files'),
    path('add_serv', views.add_srv, name='add_serv')


]