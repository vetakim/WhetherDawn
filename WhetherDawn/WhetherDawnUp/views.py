from django.shortcuts import render
from .models import Coords, Sun
from .forms import CoordsForm
from .astronomy import *
import re
# Create your views here.


def input(request):
    if request.method == "POST":
        form = CoordsForm(request.POST)
        if form.is_valid():
            coords = form.save()
        coord = Coords.objects.all().order_by('-created_date')[0]
        d_B = int(re.split(r'\D', coord.coord_B)[0])
        m_B = int(re.split(r'\D', coord.coord_B)[1])
        s_B = int(re.split(r'\D', coord.coord_B)[2])
        d_L = int(re.split(r'\D', coord.coord_L)[0])
        m_L = int(re.split(r'\D', coord.coord_L)[1])
        s_L = int(re.split(r'\D', coord.coord_L)[2])
        sun = Sun(time_rise=getDawnTime(dms2rads(d_B, m_B, s_B), dms2rads(d_L, m_L, s_L), coord.coord_H, coord.date),
                  time_set=getNightfallTime(dms2rads(d_B, m_B, s_B), dms2rads(d_L, m_L, s_L), coord.coord_H, coord.date))
        return render(request, 'WhetherDawnUp/input.html', {'results': sun, 'form': form})
    else:
        form = CoordsForm()
        return render(request, 'WhetherDawnUp/input.html', {'form': form})
