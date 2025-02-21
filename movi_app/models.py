from django.db import models
from django.db.models import Avg

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Режиссер"
        verbose_name_plural = "Режиссеры"


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    duration = models.IntegerField(verbose_name='Продолжительность')
    director = models.ForeignKey(Director, related_name='movies', on_delete=models.CASCADE, verbose_name='Режисер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильмы'
        verbose_name_plural = 'Фильмы'



STARS = (
    (i, '*' * i) for i in range(1, 6)
)

class Review(models.Model):
    text = models.TextField(max_length=500, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(default=5, choices=STARS, null=True, blank=True)

    def __str__(self):
        return f'{self.text[:30]} - {self.movie.title} - {self.stars} stars'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'