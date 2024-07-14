from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Movie, Trailer
from .serializers import MovieSerializer, TrailerSerializer


class TrailerAPIView(ListAPIView):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializer

class MovieSearch(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description','movie_file','movie_janr__name', 'davlati','categories']

    def get_queryset(self):
        queryset = super().get_queryset()
        genre_name = self.request.query_params.get('genre_name')
        if genre_name:
            queryset = queryset.filter(movie_janr__name__icontains=genre_name)
        return queryset
class MovieDetailAPIView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # permission_classes = (IsAuthenticated,)



class MoviebyCategorySearch(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['categories']

    def get_queryset(self):
        queryset = super().get_queryset()
        category_name = self.request.query_params.get('category_name')
        if category_name:
            queryset = queryset.filter(categories__icontains=category_name)
        return queryset