from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm


def news_home(request):
    news = Articles.objects.order_by('-date') #сделать ограничение по записям [:1]
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    error = ''
    if request.method == 'POST': #выполнится проверка
        form = ArticlesForm(request.POST) #получаем все данные
        if form.is_valid(): # проверяем все данные
            form.save() # сохраняем новую запись в базу
            return redirect('news_home') # выполняем переадресацию на новости
        else:
            error = 'Форма была неверной'
    form = ArticlesForm()
    
    data= {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)

    

    
    



