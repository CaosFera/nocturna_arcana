







# url PROJECT




from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls', namespace='post')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('cards/', include('cards.urls', namespace='cards')),
    path('account/', include('account.urls')),

]
