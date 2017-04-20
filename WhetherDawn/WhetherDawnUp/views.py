from django.shortcuts import render
from .models import Coords, Sun
from .forms import CoordsForm
from .astronomy import *

# Create your views here.


def input(request):
    if request.method == "POST":
        form = CoordsForm(request.POST)
        if form.is_valid():
            coords = form.save()
        coord = Coords.objects.all().order_by('-created_date')[0]
        sun = Sun(time_rise=getDawnTime(coord.coord_B, coord.coord_L, coord.coord_H, coord.date),
                  time_set=getNightfallTime(coord.coord_B, coord.coord_L, coord.coord_H, coord.date))
        return render(request, 'WhetherDawnUp/result.html', {'results': sun})
    else:
        form = CoordsForm()
        return render(request, 'WhetherDawnUp/input.html', {'form': form})


def result(request):
    return render(request, 'WhetherDawnUp/result.html')