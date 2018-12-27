from django.db import models


#slugify
class category(models.Model):
    name = models.CharField(max_length=64, blank = True, verbose_name='Название')
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name
class product(models.Model):
    name = models.CharField(max_length=64, blank = True, verbose_name='Название')
    description = models.TextField(blank = True, verbose_name='Описание')
    category = models.ForeignKey('category', blank = False, on_delete=models.CASCADE, verbose_name='Вид')
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name
"""
class knowledge_object(models.Model):
    type = models.ForeignKey('knowledge_type', blank = False, on_delete=models.CASCADE, verbose_name='Вид')
    title = models.CharField(max_length=64, blank = True, verbose_name='Заголовок')
    name = models.CharField(max_length=64, blank = True, verbose_name='Название')
    text = models.TextField(blank = True, verbose_name='Текст')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    expire_date = models.DateTimeField(default=timezone.now, verbose_name='Дата истечения')
    photo_link = models.CharField(max_length=512, blank = True, verbose_name='Ссылка')
    created_with = models.ManyToManyField("self", blank = True,symmetrical=False, verbose_name='Создано с использованием')
    knowledge_finished = models.BooleanField(default = False, verbose_name='Выполнено')
    class Meta:
        ordering = ['type']
    def __str__(self):
        return str(self.type)+' '+ self.title + ' ' + self.name
"""
# Create your models here.
