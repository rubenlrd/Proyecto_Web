from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'subtitulos', 'fecha', 'texto', 'activo', 'categoria', 'imagen', 'publicado')
    




admin.site.register(Categoria)

