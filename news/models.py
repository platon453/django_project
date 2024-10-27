from django.db import models

class Articles(models.Model): #все наследуем от моделс
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250) #чар макс 250
    full_text = models.TextField('Статья') #10-10000 тыч симв
    date = models.DateTimeField('Дата публикации')

    def __str__(self): # str метод красиво отображались
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'