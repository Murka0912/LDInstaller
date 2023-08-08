from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.





class components(models.Model):
    nameComp=models.CharField(max_length=300, verbose_name='Наименование компонента')
    nameFilepath=models.CharField(max_length=500,verbose_name='Наименование файла')
    def __str__(self):
        return self.nameComp

class srv_cat(models.Model):
    cat_id = models.IntegerField(primary_key=True, null=False)
    Name_cat = models.CharField(max_length=100)
    def __str__(self):
        return self.Name_cat

    def get_absolute_url(self):
        return reverse('Category', kwargs={'cat_id': self.cat_id})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['cat_id']

class Srv_map(models.Model):
    Namesrv = models.CharField(max_length=300, verbose_name='DNS имя сервера')
    ip_addr = models.GenericIPAddressField(verbose_name='IP адрес сервера' )
    Category = models.ForeignKey(srv_cat,verbose_name='Назначение сервера', on_delete=models.CASCADE)
    username = models.CharField(verbose_name='Имя пользователя',max_length=100)
    password = models.CharField(verbose_name='Пароль',max_length=100)
    components = models.ManyToManyField(components,verbose_name='Компоненты для установки', null=True)
    def __str__(self):
        return self.Namesrv

class Configuration(models.Model):
    HostAppServer=  models.CharField(max_length=300, verbose_name='Адрес СК')
    HostKafka= models.CharField(max_length=300, verbose_name='Адрес кафки')
    HostScheduler=  models.CharField(max_length=300, verbose_name='адрес планировщика')
    HostSecurityServer= models.CharField(max_length=300, verbose_name='Наименование файла')
    HostPSO= models.CharField(max_length=300, verbose_name='Наименование файла')
    HostMEDO= models.CharField(max_length=300, verbose_name='Наименование файла')
    DataBaseType= models.CharField(max_length=300, verbose_name='Наименование файла')
    DataBaseHost= models.CharField(max_length=300, verbose_name='Наименование файла')
    DataBaseName= models.CharField(max_length=300, verbose_name='Наименование файла')
    DBConnetionLogin= models.CharField(max_length=300, verbose_name='Наименование файла')
    DBConnetionPassword= models.CharField(max_length=300, verbose_name='Наименование файла')


