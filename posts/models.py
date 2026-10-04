from django.db import models

from users.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=128,
      )
    text = models.TextField(
        verbose_name='Текст поста',
        max_length=512,
      )
    created = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add= True,
    )
    updated = models.DateTimeField(
        verbose_name='Время изменения',
        auto_now= True,
    )
    author = models.ForeignKey(
        to=User,
        verbose_name='Автор',
        on_delete= models.CASCADE,
        related_name='posts'

    )
    

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'


    





    