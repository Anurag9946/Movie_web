from movieapp.models import Movies
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .models import Movie, Movieitem

def _movie_id(request):
    film = request.session.session_key
    if not film:
        film = request.session.create()
    return film

def add_list(request, film_id):
    movie = Movies.objects.get(id=film_id)

    try:
        film = Movie.objects.get(cinema_id=_movie_id(request))
    except Movie.DoesNotExist:
        film = Movie.objects.create(
            cinema_id=_movie_id(request)
        )
        film.save()
    try:
        movie_item = Movieitem.objects.get(movie=movie, film=film)

    except Movieitem.DoesNotExist:
        movie_item = Movieitem.objects.create(
            movie=movie,
            quantity=1,
            film=film
        )
        movie_item.save()

    return redirect('wishlist:movies_detail')

def movies_detail(request, movie_items=None):
    try:
        film = Movie.objects.get(cinema_id=_movie_id(request))
        movie_items = Movieitem.objects.filter(film=film, active=True)
    except ObjectDoesNotExist:
        pass

    return render(request, 'wishlist.html', {'movie_items': movie_items})

def delete(request, film_id):
    film = Movie.objects.get(cinema_id=_movie_id(request))
    movie =  get_object_or_404(Movies,id=film_id)
    movie_item = Movieitem.objects.get(movie=movie,film=film)
    movie_item.delete()

    return redirect('wishlist:movies_detail')
