from django.db import models
from movieapp.models import Movies
# Create your models here.


class Movie(models.Model):
    cinema_id = models.CharField(max_length=250,blank=True)
    date_added = models.DateField(auto_now_add=True)


    class Meta:
        db_table = 'Movie'
        ordering = ['date_added']

    def __str__(self):
        return '{}'.format(self.cinema_id)

class Movieitem(models.Model):
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE)
    film = models.ForeignKey(Movie,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Movieitem'

    def __str__(self):
        return '{}'.format(self.movie)


