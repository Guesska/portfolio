from django.db import models


class AboutMe(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    image = models.ImageField(upload_to='images/about_me/%Y/%m/%d/', blank=True, verbose_name='Изображение')


    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'


class Skills(models.Model):
    title = models.CharField(max_length=255, verbose_name='Навык')
    content = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/skills/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    updated_at = models.DateTimeField(auto_now=True)
    ordering = models.IntegerField(verbose_name="Очередность", default=0)

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
        ordering = ['ordering']

    def __str__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=255, verbose_name='Проект')
    content = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/projects/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    url = models.URLField(verbose_name='Url')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title
