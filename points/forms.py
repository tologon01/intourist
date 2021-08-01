from django import forms
from django.forms import fields
from .models import Points

class PointsForm(forms.ModelForm):
    class Meta:
        model = Points
        fields = ['name', 'location', 'description']