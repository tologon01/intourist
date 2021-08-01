from django.urls import path
from django.urls.resolvers import URLPattern
from .views import points, create_points, point, \
    edit_point, delete_point 

urlpatterns = [
    path('', points, name='points-list'),
    path('create/', create_points, name='create-points'),
    path('<int:id>/', point, name='point'),
    path('<int:id>/edit/', edit_point, name='edit-point'),
    path('<int:id>/delete/', delete_point, name='delete-point')
] 
