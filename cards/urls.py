from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cards'

urlpatterns = [

    path('tarot_history/', views.tarot_history, name='tarot_history'),
    path('major_arcana_home/', views.major_arcana_home, name='major_arcana_home'),
    path('major_arcana_list/', views.major_arcana_list, name='major_arcana_list'),
    path('major_arcana/<slug:slug>/', views.major_arcana_detail, name='major_arcana_detail'),
    path('minor_arcana_home/', views.minor_arcana_home, name='minor_arcana_home'),
    path('enumerators_list/', views.enumerators_list, name='enumerators_list'),
    path('enumerators/<slug:slug>/', views.enumerators_detail, name='enumerators_detail'),
    path('corte_list/', views.corte_list, name='corte_list'),
    path('corte/<slug:slug>/', views.corte_detail, name='corte_detail'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
