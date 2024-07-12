from rest_framework import serializers
from .models import Movie, Trailer, Photo, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image', 'created_at', 'updated_at']

class TrailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trailer
        fields = ['id', 'video_url', 'created_at', 'updated_at']

class MovieSerializer(serializers.ModelSerializer):
    trailers = TrailerSerializer(many=True, read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description',
                  'updated_at', 'trailers', 'photos', 'categories','movie_file',
                  'release_date', 'created_at',
                  ]
