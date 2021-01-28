from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'full_name', 'categories', 'deleted'] # mostra tudo
    search_fields = ['title', 'subtitle'] # Adiciona campo de busca nos posts
    #fields = ['title', 'subtitle'] # Mostra ou esconde o conteúdo do post

    #def get_queryset(self, request): # Função que mostra o post aprovado
    #   return Post.objects.filter(deleted=False)

admin.site.register(Post, PostAdmin)
