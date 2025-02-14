from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def movies_count(self):
        return Movie.objects.filter(director=self).count()

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField()
    director = models.ForeignKey(Director,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

STARS = (
    (i, '* ' * i)for i in range(1,6)
)

class Review(models.Model):
    title = models.CharField(max_length=500)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='reviews')
    stars = models.IntegerField(default=5,choices=STARS)

    def __str__(self):
        return f'{self.movie.title}-{self.stars} stars'
