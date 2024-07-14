from django.contrib import admin
from .models import Movie, Trailer,MovieJanr

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','image')
    list_filter = ( 'categories',)
    search_fields = ('title', 'description')
    filter_horizontal = (['movie_janr'])

admin.site.register(Movie, MovieAdmin)
admin.site.register(Trailer)
# admin.site.register(Photo)
# admin.site.register(Category)
admin.site.register(MovieJanr)