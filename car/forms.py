from django.forms import ModelForm, Form, ChoiceField, CharField, IntegerField, BooleanField
from django.forms import models
from django.forms import fields
from django.forms.widgets import TextInput, Select
from .models import Car, GEARBOX_CHOICES

class CarForm(Form):
    manufacturer = CharField(max_length=50, required=False, widget=TextInput(attrs={'placeholder': 'ВАЗ', 'class': 'form-control form-control-sm'}))
    car_model = CharField(max_length=50, required=False, widget=TextInput(attrs={'placeholder': '2110', 'class': 'form-control form-control-sm'}))
    year = IntegerField(required=False, widget=TextInput(attrs={'placeholder': '1980', 'class': 'form-control form-control-sm w-50', 'style': 'display: inline'}))
    gearbox = ChoiceField(choices=GEARBOX_CHOICES + [(4, 'Любая')], required=False, widget=Select(attrs={'class': 'form-control form-control-sm'}), initial=4)
    color = CharField(required=False, widget=TextInput(attrs={'type': 'color'}))
    year_choices = ChoiceField(choices=[('__lt','<'), ('__gt','>'), ('','=')], required=False, widget=Select(attrs={'class': 'form-control form-control-sm w-25', 'style': 'display: inline'}))
    color_checked = BooleanField(required=False)

class CarAdminForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }

