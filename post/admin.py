from django.contrib import admin
from .models import Post, Comment, Response, SiteLogo, Category, Home


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
   

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created', 'updated', 'image', 'body_post', 'slug')
    list_filter = ('status', 'created', 'user_post')
    search_fields = ('title', 'body_post')    
    date_hierarchy = 'created'    
    raw_id_fields = ['user_post']
    ordering = ('created',)    
    prepopulated_fields = {'slug': ('title',)}
    
    


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_comment', 'post_comment', 'created', 'active', 'body_comment', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('user_comment', 'body_comment')

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('user_response', 'response_comment', 'created', 'active', 'response', )
    list_filter = ('active', 'created', 'updated')
 
    search_fields = ('user_response', 'body_response')


@admin.register(SiteLogo)
class SiteLogoAdmin(admin.ModelAdmin):
    list_display = ('logo',)

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('img1', 'img2', 'img3', 'img4')