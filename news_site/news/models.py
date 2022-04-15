from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # добавятся дата и время и редактироваться больше не будут
    updated_at = models.DateTimeField(auto_now=True)  # будут редактироваться при каждом редактирование записи
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')  # сохр. путь до img, указ. путь разбивается на папки по д.
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
