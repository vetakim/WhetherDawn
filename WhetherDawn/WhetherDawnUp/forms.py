from django import forms
from .models import Coords


class CoordsForm(forms.ModelForm):

    class Meta:
        model = Coords
        fields = ('coord_B', 'coord_L', 'coord_H')
