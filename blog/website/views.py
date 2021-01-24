from django.shortcuts import render


# Create your views here.
def hello_blog(request):
    lista = ['Python', 'Git', 'Django', 'Linux', 'Banco de Dados', 'HTML']
    data = {'name': 'Curso de Django 3', 'lista_tecnologia': lista}
    return render(request, 'indexgeral.html', data)