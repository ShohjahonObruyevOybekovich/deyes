from django.urls import path
from main.views import *
urlpatterns = [
    # path('movie-get/', MovieMenuAPIView.as_view(), name='movie-get'),

    path('Trailer-get/', TrailerAPIView.as_view(), name='trailer-get'),

    # path('Photo-get/', PhotoAPIView.as_view(), name='photo-get'),

    # path('Category-get/', CategoryAPIView.as_view(), name='category-get'),
    # path('search-category/', CategorySearch.as_view(), name='cearch_category'),
    path('movie-search/', MovieSearch.as_view(), name='movie_search'),
    path('movies/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),

    # Other URL patterns...
    path('movies/by-category/', MoviebyCategorySearch.as_view(), name='movie-by-category'),
]