from django.contrib import admin
from .models import Profile, Rating, BannersProfile




@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('photo', 'biographia', 'instagram', 'facebook', 'whatsapp',\
                     'telegram', 'slug', 'user', 'average_rating', 'total_rating')

@admin.register(BannersProfile)
class BannersProfilegAdmin(admin.ModelAdmin):
    list_display = ('profile', 'banners')
    


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('profile', 'user', 'comment', 'created', 'rating')
    