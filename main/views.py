from django.shortcuts import render
#from django.http import HttpResponse # класс для вывода

def index(request): #параметр реквест
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data)


def about(request): #параметр реквест
    return render(request, 'main/about.html')
    
