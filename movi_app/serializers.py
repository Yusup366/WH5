from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = ['id','name','movie_count']

    def get_movie_count(self, director):
        return director.movies.count()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','text','movie','stars']


class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    director = DirectorSerializer()
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id','title','description','duration','director','reviews','average_rating']

    def get_average_rating(self, movie):
        reviews = movie.reviews.all()
        if reviews:
            sum_reviews = sum([review.stars for review in reviews])
            average = sum_reviews / len(reviews)
            return average
        return None


