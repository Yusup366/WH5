from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.ReadOnlyField(source='movies.count')
    class Meta:
        model = Director
        fields = [' name',' movies_count']

    def get_movies_count(self, movie):
        return movie.movies.count()

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = [' title',' description',' duration',' director']


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    class Meta:
        model = Review
        fields = ['movie',' text',' stars']