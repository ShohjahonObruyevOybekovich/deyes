from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MovieJanr(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name='movies')
    movie_janr = models.ManyToManyField(MovieJanr, related_name='movies')
    movie_telegram_code  = models.CharField(max_length=100, blank=True,null=True)
    movie_file = models.FileField(upload_to='movies/', blank=True, null=True)
    davlati = models.FloatField(blank=True, null=True)
    language =models.CharField(max_length=100)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Trailer(models.Model):
    movie = models.ForeignKey(Movie, related_name='trailers', on_delete=models.CASCADE)
    video_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Trailer for {self.movie.title}"

class Photo(models.Model):
    movie = models.ForeignKey(Movie, related_name='photos', on_delete=models.CASCADE)
    image = models.FileField(upload_to='movie_photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Photo for {self.movie.title}"
