from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import FormView, DetailView
from .models import Feedback, Points
from .forms import PointsForm, FeedbackForm


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
    try:
        point_object = Points.objects.get(id=id)
        return render(request, 'points/point.html', {'point_object': point_object})
    except Points.DoesNotExist as e:
        return HttpResponse(f'Not found:   {e}', status=404)
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

class FeedbackView(FormView):
    template_name = 'points/feedback_form.html'
    form_class = FeedbackForm
    success_url = '/Points/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class FeedbackDetailView(DetailView):
    queryset = Feedback.objects.all()
    template_name = 'points/feedback.html'