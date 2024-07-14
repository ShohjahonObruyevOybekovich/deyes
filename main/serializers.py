from rest_framework import serializers
from .models import Movie, Trailer


class TrailerSerializer(serializers.ModelSerializer):
    movie_id = serializers.SerializerMethodField()

    class Meta:
        model = Trailer
        fields = ['id', 'video_url', 'movie_id']

    def get_movie_id(self, obj):
        return obj.movie.id if obj.movie else None

class MovieSerializer(serializers.ModelSerializer):
    # categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description','image',
                  'categories','movie_file','language',
                  'davlati','movie_janr','release_date'
                  ]

