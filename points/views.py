from django.shortcuts import render, redirect
from .models import Points
from .forms import PointsForm


def points(request):
    points_objects = Points.objects.all()
    return render(request, 'points/points.html', {'pointes': points_objects})

def create_points(request):
    if request.method == "POST":
        points_form = PointsForm(request.POST)
        if points_form.is_valid():
            points_form.save()
            return redirect(points)

    points_form = PointsForm()
    return render(request, 'points/form.html', {'points_form': points_form})

def point(request, id):
    point_object = Points.objects.get(id=id)
    return render(request, 'points/point.html', {'point_object': point_object})

def edit_point(request, id):
    point_object = Points.objects.get(id=id)

    if request.method == 'POST':
        points_form = PointsForm(data=request.POST, instance=point_object)
        if points_form.is_valid():
            points_form.save()
            return redirect(point, id=id)

    points_form = PointsForm(instance=point_object)
    return render(request, 'points/form.html', {'points_form': points_form})


def delete_point(request, id):
    point_object = Points.objects.get(id=id)
    point_object.delete()
    return redirect(points)