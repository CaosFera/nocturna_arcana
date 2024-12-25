from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'post'

urlpatterns = [
    path('', views.home, name='home'),
    path('post_list', views.post_list, name='post_list'),
    path('category_list', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.post_category, name='post_category'),   
    path('<int:year>/<int:month>/<int:day>/<int:id>/<slug:post>/', views.post_detail, name='post_detail'),
    path('search/', views.post_search, name='post_search'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('comment/<int:post_id>/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
    path('comment/<int:post_id>/<int:comment_id>/edit/', views.comment_edit, name='comment_edit'),
    path('response/<int:post_id>/<int:comment_id>/', views.response_comment, name='response_comment'),
    path('contribua/', views.contribua, name='contribua'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


