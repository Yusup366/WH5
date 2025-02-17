from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = ['id','name','movie_count']

    def get_movie_count(self, director):
        return director.movies.count()

    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Имя должно содержать только буквы.")

        if Director.objects.filter(name=value).exists():
            raise serializers.ValidationError('Режисер с таким именем уже существует.')
        return value

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','text','movie','stars']
    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError('Звезды должны быть от 1 до 5.')
        return value


class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    director = serializers.PrimaryKeyRelatedField(queryset=Director.objects.all())
    reviews = ReviewSerializer(many=True, read_only=True)
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

    def validate_director(self, value):
        if not Director.objects.filter(id=value.id).exists():
            raise serializers.ValidationError('Режиссер с таким id не существует.')
        return value

    def validate_reviews(self, value):
        if value <= 0:
            raise serializers.ValidationError('Продолжительность филма должна быть положительной')
        return value
