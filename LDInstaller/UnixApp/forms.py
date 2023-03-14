from django.forms import ModelForm, TextInput, Select, ChoiceField, ModelChoiceField, CheckboxSelectMultiple,MultipleChoiceField

from .models import *
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
class RegForm(ModelForm):
    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    class Meta:
        model = Srv_map
        fields = ['Namesrv','ip_addr','Category','username','password','components']
        favorite_colors = MultipleChoiceField(
            required=False,
            widget=CheckboxSelectMultiple,
            choices=FAVORITE_COLORS_CHOICES,

        )
        con_cat = ModelChoiceField(queryset=components.objects.all(),widget=CheckboxSelectMultiple, empty_label='fffff', to_field_name='components')
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
            })





        }