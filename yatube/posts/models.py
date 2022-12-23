from django.contrib.auth.models import User
from django.db import models


class Group(models.Model):
    title = models.CharField('Название группы', max_length=200)
    slug = models.SlugField('URL адрес', default='some string',
                            unique=True)
    description = models.TextField('Описание группы',
                                   max_length=10000,
                                   default='some string', )

    class Meta:
        verbose_name = 'Группы'
        verbose_name_plural = 'Группы'
        ordering = ('-id',)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField('Текст поста')
    pub_date = models.DateTimeField('Дата публикации',
                                    auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posts',
                               verbose_name='Автор')
    group = models.ForeignKey(Group, blank=True, null=True,
                              on_delete=models.SET_NULL,
                              related_name='posts',
                              verbose_name='Группа')

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'Сортировка по дате публикации'

    def __str__(self):
        return self.text[0:30]
