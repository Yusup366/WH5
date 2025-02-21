from django.contrib import admin
from .models import Director,Movie,Review


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','duration','director',)
    search_fields = ('title',)
    list_filter = ('director',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie','text','stars',)

admin.site.register(Director)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Review,ReviewAdmin)


