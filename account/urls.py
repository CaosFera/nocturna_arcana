from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [

        
        path('login/', auth_views.LoginView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
        path('password-change/done/',  auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
        path('password-reset/', auth_views.PasswordResetView.as_view(),  name='password_reset'),
        path('password-reset/done/',  auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
        path('password-reset/<uidb64>/<token>/',  auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
        path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(),  name='password_reset_complete'),
        path('dashboard/', views.dashboard, name='dashboard'),
        path('create_profile/', views.create_profile, name='create_profile'),
        path('edit_profile/', views.edit_profile, name='edit_profile'),
        path('register/', views.register, name='register'),
        path('list_profile/', views.list_profile, name='list_profile'),
        path('profile_detail/<slug:slug>/', views.profile_detail, name='profile_detail'),
        path('create_post/', views.create_post, name='create_post'),
        path('create_category/', views.create_category, name='create_category'),
        path('my_posts/', views.my_posts, name='my_posts'),       
        path('delete_post<int:year>/<int:month>/<int:day>/<int:id>/<slug:post>/', views.delete_post, name='delete_post'),
        path('edit_post<int:year>/<int:month>/<int:day>/<int:id>/<slug:post>/', views.edit_post, name='edit_post'),
        path('update_rating/<slug:slug>/', views.update_rating, name='update_rating'),
        path('profile_prices/<slug:slug>/', views.profile_prices, name='profile_prices'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
