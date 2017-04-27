from django.shortcuts import render
from .forms import CoordsForm, Cities
from .astronomy import *
import re
# Create your views here.


def input(request):
    if request.method == "POST":
        form = CoordsForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            d_B = int(re.split(r'\D', f['coord_B'])[0])
            m_B = int(re.split(r'\D', f['coord_B'])[1])
            s_B = int(re.split(r'\D', f['coord_B'])[2])
            d_L = int(re.split(r'\D', f['coord_L'])[0])
            m_L = int(re.split(r'\D', f['coord_L'])[1])
            s_L = int(re.split(r'\D', f['coord_L'])[2])
            a = getDawnTime(dms2rads(d_B, m_B, s_B), dms2rads(d_L, m_L, s_L), f['coord_H'], f['date'])
            b = getNightfallTime(dms2rads(d_B, m_B, s_B), dms2rads(d_L, m_L, s_L), f['coord_H'], f['date'])
            sun = {'time_rise': a, 'time_set': b}
            city = Cities()
            return render(request, 'WhetherDawnUp/input.html', {'results': sun, 'form': form, 'city': city})
    else:
        form = CoordsForm()
        city = Cities()
        return render(request, 'WhetherDawnUp/input.html', {'form': form, 'city': city})
