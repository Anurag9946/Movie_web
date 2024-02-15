

from . import views
from django.urls import path

app_name = 'movieapp'

urlpatterns = [

    path('', views.index,name='index'),
    path('sports/', views.sports,name='sports'),
    path('detail/<int:movie_id>/', views.detail, name='detail'),
    path('sport_detail/<int:sport_id>/', views.sport_detail, name='sport_detail'),
    path('add/', views.add_movie, name= 'add_movie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),

]












#
# from django.contrib import admin
# from django.urls import include, path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('movieapp/', include('movieapp.urls', namespace='movieapp')),
#     # other paths...
# ]














