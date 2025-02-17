from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField()
    director = models.ForeignKey(Director,related_name='movies',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

STARS = (
    (i, '*' * i) for i in range(1, 6)
)

class Review(models.Model):
    text = models.TextField(max_length=500,null=True,blank=True)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='reviews')
    stars = models.IntegerField(default=5,choices=STARS,null=True,blank=True)

    def __str__(self):
        return f'{self.text[:30]}-{self.movie.title}-{self.stars} stars'
