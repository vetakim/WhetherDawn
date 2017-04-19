from django.shortcuts import render
from .models import Coords
from django.shortcuts import redirect
from .forms import CoordsForm

# Create your views here.


def input(request):
    if request.method == "POST":
        form = CoordsForm(request.POST)
        if form.is_valid():
            coords = form.save()
            a = Coords.objects.all().order_by('-created_date')[0]
            return render(request, 'WhetherDawnUp/result.html', {'results': a})
    else:
        form = CoordsForm()
        return render(request, 'WhetherDawnUp/input.html', {'form': form})


def result(request):
    return render(request, 'WhetherDawnUp/result.html')