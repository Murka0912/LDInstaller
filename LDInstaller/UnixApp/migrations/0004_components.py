# Generated by Django 4.1.7 on 2023-03-13 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UnixApp', '0003_srv_map_password_srv_map_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='components',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameComp', models.CharField(max_length=300, verbose_name='Наименование компонента')),
                ('nameFilepath', models.CharField(max_length=500, verbose_name='Наименование файла')),
            ],
        ),
    ]
