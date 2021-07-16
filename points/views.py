from django.shortcuts import render
from .models import Points
# Create your views here.

def points(request):
    points_objects = Points.objects.all()
    return render(request, 'index.html', {'pointes': points_objects})