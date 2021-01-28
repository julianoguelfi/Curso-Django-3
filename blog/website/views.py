from django.shortcuts import render
from .models import Post

# Create your views here.
def hello_blog(request):
    lista = ['Python', 'Git', 'Django', 'Linux', 'Banco de Dados', 'HTML']

    list_posts = Post.objects.filter(deleted=False)

    data = {'name': 'Curso de Django 3',
            'lista_tecnologia': lista,
            'posts': list_posts }
    return render(request, 'index.html', data)