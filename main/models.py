import random

from django.db import models

class MovieJanr(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to='movie_photos/',null=True)
    MULTIFILM = 'ml'
    SERIAL = 'sr'
    KINO = 'kn'
    CATEGORY_CHOICES = [
        (MULTIFILM, 'Multifilm'),
        (SERIAL, 'Serial'),
        (KINO, 'Kino'),
    ]

    categories = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default=KINO,
    )
    movie_janr = models.ManyToManyField(MovieJanr, related_name='movies')
    # movie_telegram_code = models.IntegerField(default=random.randint(10000, 99999))

    # def save(self, *args, **kwargs):
    #     if not self.movie_telegram_code:
    #         self.movie_telegram_code = str(random.randint(10000, 99999))
    #     super().save(*args, **kwargs)
    movie_file = models.FileField(upload_to='movies/', blank=True, null=True)
    UZB = 'UZB'
    USA = 'USA'
    CANADA = 'CAN'
    UK = 'UK'
    GERMANY = 'GER'
    FRANCE = 'FRA'
    ITALY = 'ITA'
    SPAIN = 'ESP'
    JAPAN = 'JPN'
    CHINA = 'CHN'
    INDIA = 'IND'
    BRAZIL = 'BRA'
    AUSTRALIA = 'AUS'

    COUNTRY_CHOICES = [
        (UZB, 'Uzbekiston'),
        (USA, 'United States'),
        (CANADA, 'Canada'),
        (UK, 'United Kingdom'),
        (GERMANY, 'Germany'),
        (FRANCE, 'France'),
        (ITALY, 'Italy'),
        (SPAIN, 'Spain'),
        (JAPAN, 'Japan'),
        (CHINA, 'China'),
        (INDIA, 'India'),
        (BRAZIL, 'Brazil'),
        (AUSTRALIA, 'Australia'),
    ]

    davlati = models.CharField(
        max_length=3,
        choices=COUNTRY_CHOICES,
        blank=True,
        null=True,
    )
    ENGLISH = 'eng'
    RUSSIAN = 'ru'
    UZBEK = 'uz'
    LANGUAGE_CHOICES = [
        (ENGLISH, 'English'),
        (RUSSIAN, 'Russian'),
        (UZBEK, 'Uzbek'),
    ]

    language = models.CharField(
        max_length=100,
        choices=LANGUAGE_CHOICES,
        default=ENGLISH,
    )
    release_date = models.DateField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Trailer(models.Model):
    movie = models.ForeignKey(Movie, related_name='trailers', on_delete=models.CASCADE)
    video_url = models.URLField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Trailer for {self.movie.title}"



