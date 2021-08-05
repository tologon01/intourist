from django import forms
from django.forms import fields
from .models import Points, Feedback

class PointsForm(forms.ModelForm):
    class Meta:
        model = Points
        fields = ['name', 'location', 'description']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('point', 'text')