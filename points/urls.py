from django.urls import path
from django.urls.resolvers import URLPattern
from .views import points
urlpatterns = [
    path('', points, name='points-list')
] 