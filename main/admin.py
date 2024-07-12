from django.contrib import admin
from .models import Movie, Trailer, Photo, Category,MovieJanr

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date','movie_telegram_code','created_at', 'updated_at')
    list_filter = ('release_date', 'categories')
    search_fields = ('title', 'description')
    filter_horizontal = (['categories','movie_janr'])

admin.site.register(Movie, MovieAdmin)
admin.site.register(Trailer)
admin.site.register(Photo)
admin.site.register(Category)
admin.site.register(MovieJanr)