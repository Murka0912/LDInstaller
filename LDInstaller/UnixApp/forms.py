from django.forms import ModelMultipleChoiceField,CharField,ModelForm,SelectMultiple, TextInput, Select, ChoiceField, ModelChoiceField, CheckboxSelectMultiple,MultipleChoiceField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *



class TableDataForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'my_from'
        self.helper.form_class = 'search'
        self.helper.form_method = 'post'



    components = ModelMultipleChoiceField(
        queryset=components.objects.all().order_by('nameComp'),
        label="Выбор компнонента для установки",
        widget=SelectMultiple(attrs={'class':'form-inner'}),
        required=False,
        )
    Category = ModelChoiceField(queryset=srv_cat.objects.all(),label='Назначение сервера', widget=Select, required=False)

    class Meta:

        model = Srv_map

        fields = ['Namesrv','Category','ip_addr','username','password', 'components']

        widgets = {
            'Namesrv': TextInput(attrs={
                'placeholder': 'DNS имя',
                'style': '-moz-placeholder',
                'required':"False"
            }),
            'ip_addr': TextInput(attrs={
                'placeholder': 'IP addres'
            }),
            'Category': TextInput(attrs={
                'placeholder': 'Тип сервера'
            }),
            'username': TextInput(attrs={
                'placeholder': 'логин'
            }),
            'password': TextInput(attrs={
                'type':'password',
                
                'placeholder': 'пароль'
            }),
            'Components': TextInput(attrs={
                'type': 'checkbox',
                'class':'custom-radio',
                'placeholder': 'Пароль'
            })
        }


