from django.contrib import admin
from .models import MajorArcana, MinorArcana, Corte, Tarot

admin.site.site_header = "NOCTURNA ARCANA"
admin.site.site_title = "Seja bem vindo área administrativa!"
admin.site.index_title = "Título Personalizado do Rodapé do Site"

@admin.register(Tarot)
class TarotArcanaAdmin(admin.ModelAdmin):
    list_display = ('title',  'image_tarot', 'text_body')


@admin.register(MajorArcana)
class MajorArcanaAdmin(admin.ModelAdmin):
    list_display = ('name_major_arcana',  'description', 'image_major', 'slug')
    list_filter = ('name_major_arcana', )
    search_fields = ('name_major_arcana',)    
    ordering = ('name_major_arcana',)    
    prepopulated_fields = {'slug': ('name_major_arcana',)}
    
@admin.register(MinorArcana)
class MinorArcanaAdmin(admin.ModelAdmin):
    list_display = ('name_minor_arcana', 'description', 'slug', 'image_minor', 'icone')
    prepopulated_fields = {'slug': ('name_minor_arcana',)}
    ordering = ('name_minor_arcana',)    

@admin.register(Corte)
class CorteAdmin(admin.ModelAdmin):
    list_display = ('icone', 'name_corte', 'image_corte', 'description', 'slug')
    ordering = ('name_corte',)    
    prepopulated_fields = {'slug': ('name_corte', )}
    