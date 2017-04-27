from django import forms
from datetime import date
from .models import City

class CoordsForm(forms.Form):
    coord_B = forms.CharField(max_length=10, initial='55°45′07″')
    coord_L = forms.CharField(max_length=10, initial='37°36′56″')
    coord_H = forms.FloatField(initial=144)
    date = forms.DateField(initial=date.today)


class Cities(forms.Form):
    choises = (
        (1, 'Msk'),
        (2, 'Spb'),
    )
    a = ((i, i) for i in City.objects.all())
    City = forms.ChoiceField(choices=a)
