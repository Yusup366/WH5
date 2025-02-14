from django.db.models.aggregates import Avg
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie , Review
from .serializers import DirectorSerializer,MovieSerializer,ReviewSerializer

@api_view(['GET'])
def director_detail_api_view(request,id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error':'Director not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(director).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def director_list_api_view(request,id):
    directors = Director.objects.all(id=id)
    data = DirectorSerializer(directors,many=True).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def director_movie_count(request):
    directors = Director.objects.annotate(movie_count=Count('movie'))
    directors_data = DirectorSerializer(directors,many=True).data
    return Response(directors_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_detail_api_view(request,id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error':'Movie not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializer(movie).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies,many=True).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_review_list_api_view(request):
    movies = Movie.objects.all()
    movie_data = []
    for movie in movies:
        review = Review.objects.filter(movie=movie)
        avg_rating = review.aggregate(Avg('stars'))['stars__avg'] or 0
        movie_data.append({'movie': MovieSerializer(movie).data, 'rating':
            avg_rating,'review': ReviewSerializer(review,many=True).data})
    return Response(movie_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_detail_api_view(request,id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error':'Review not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(review).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews,many=True).data
    return Response(data=data, status=status.HTTP_200_OK)




