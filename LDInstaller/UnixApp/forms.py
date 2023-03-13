from django.forms import ModelForm, TextInput, Select, ChoiceField, ModelChoiceField

from .models import *

class RegForm(ModelForm):
    class Meta:
        model = Srv_map
        fields = ['Namesrv','ip_addr','Category','username','password','components']
        #con_cat = ModelChoiceField(queryset=components.objects.all(), empty_label='fffff', to_field_name='cat')
        widgets ={
            'Name_srv':TextInput(attrs={
                'placeholder':'Адрес сервера',
                'style':'-moz-placeholder'
            }),
            'ip_addr':TextInput(attrs={
                'placeholder':'ip address',
                'style':'-moz-placeholder'
            }),
            'Category':TextInput(attrs={
                'placeholder':'Назначение сервера',
                'style':'-moz-placeholder'
            }),
            'username': TextInput(attrs={
                'placeholder': 'username',
                'style': '-moz-placeholder'
            }),
            'password': TextInput(attrs={
                'placeholder': 'password',
                'style': '-moz-placeholder'
            }),



        }