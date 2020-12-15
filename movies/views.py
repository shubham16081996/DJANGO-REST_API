from django.shortcuts import render

from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import AllMovies

# Create your views here.


def index(request):
    return render(request, 'movies/index.html')


class MovieView(viewsets.ModelViewSet):
    queryset = AllMovies.objects.all()
    serializer_class = MovieSerializer


class ActionView(viewsets.ModelViewSet):
    queryset = AllMovies.objects.filter(Type='Action')
    serializer_class = MovieSerializer


class ComedyView(viewsets.ModelViewSet):
    queryset = AllMovies.objects.filter(Type='Comedy')
    serializer_class = MovieSerializer


class CrimeView(viewsets.ModelViewSet):
    queryset = AllMovies.objects.filter(Type='Crime')
    serializer_class = MovieSerializer


class DramaView(viewsets.ModelViewSet):
    queryset = AllMovies.objects.filter(Type='Drama')
    serializer_class = MovieSerializer



