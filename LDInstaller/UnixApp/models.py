from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Srv_map(models.Model):
    Namesrv = models.CharField(max_length=300, verbose_name='DNS имя сервера')
    ip_addr = models.GenericIPAddressField(verbose_name='IP адрес сервера' )
    Category = models.CharField(verbose_name='Назначение сервера',max_length=100)
    username = models.CharField(verbose_name='UserName',max_length=100)
    password = models.CharField(verbose_name='password',max_length=100)
    components = models.CharField(verbose_name='Components',max_length=1000)


class components(models.Model):
    nameComp=models.CharField(max_length=300, verbose_name='Наименование компонента')
    nameFilepath=models.CharField(max_length=500,verbose_name='Наименование файла')

