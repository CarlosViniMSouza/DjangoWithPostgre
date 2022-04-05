from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm


def form_view(request):
    form = CarForm()
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'templates/home.html', {'form': form})
