from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Name of the news', db_index=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Publication date')  # добавятся дата и время и ред. больше не будут
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Update date')  # будут редакт. при каждом редактирование записи
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',
                              blank=True)  # сохр. путь до img, указ. путь разбивается на папки по д.
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True)
    # название модели передаём как строку, если она определена позже

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'  # название новости в ед.ч. в админке
        verbose_name_plural = 'List of news'  # Название в мн.ч в админке
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='News category')

    class Meta:
        verbose_name = 'News category'
        verbose_name_plural = 'News categories'
        ordering = ['title']

    def __str__(self):
        return self.title
