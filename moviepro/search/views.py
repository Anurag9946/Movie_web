from django.shortcuts import render
from movieapp.models import Movies,Sports

from django.db.models import Q

def search_result(request):
    movie = None
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        movie = Movies.objects.all().filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'search.html', {'query': query, 'movie': movie})



