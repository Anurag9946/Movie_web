

from . import views
from django.urls import path

app_name = 'wishlist'

urlpatterns = [
    path('add/<int:film_id>/', views.add_list, name='add_list'),
    path('', views.movies_detail, name='movies_detail'),
    path('delete/<int:film_id>/' ,views.delete,name='delete'),

]

