from django.db.models.deletion import PROTECT
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from main.models import Cinema, Movie
from rest_framework.response import Response
from .serializers import FilmSerializer, MovieCreateValidateSerializer

@api_view(['GET', 'POST'])
def film_list_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = FilmSerializer(movies, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = MovieCreateValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={'message': 'error', 'errors': serializer.errors})
        title = request.data['title']
        description = request.data['description']
        cinema = request.data['cinema']
        genres = request.data['genres']
        movie = Movie.objects.create(
            title=title, description=description, cinema_id=cinema,
        )
        movie.save()
        movie.genres.set(genres)
        movie.save()
        return Response("Movie succesfully added!")

@api_view(['GET', 'PUT', 'DELETE'])
def film_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'eror':'Movie not found'})
    if request.method == 'GET':
        serializer = FilmSerializer(movie, many=False)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        serializer = MovieCreateValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={'message': 'error', 'errors': serializer.errors})
        movie.title == request.data['title']
        movie.description == request.data['description']
        movie.cinema == request.data['cinema']
        movie.genres.set(request.data['genres'])
        movie.save()
        return Response(data={'massage': 'Movie updated!'})
    else:
        movie.delete()
        return Response()
