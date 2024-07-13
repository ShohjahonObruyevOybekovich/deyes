from rest_framework import viewsets, filters, permissions
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Movie, Trailer, Photo, Category
from .serializers import MovieSerializer, TrailerSerializer, PhotoSerializer, CategorySerializer

class MovieMenuAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'categories__name']

class TrailerAPIView(ListAPIView):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializer


class PhotoAPIView(ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategorySearch(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class MovieSearch(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'movie_janr__name', 'davlati']

    def get_queryset(self):
        queryset = super().get_queryset()
        genre_name = self.request.query_params.get('genre_name')
        if genre_name:
            queryset = queryset.filter(movie_janr__name__icontains=genre_name)
        return queryset
