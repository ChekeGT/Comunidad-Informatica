from django.db import models
from django.contrib.auth.models import  User

# Create your models here.


class Comment(models.Model):
    text = models.TextField(verbose_name='Texto:')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='writer')
    created = models.DateTimeField(verbose_name='Fecha De Creacion:',auto_now_add=True, editable=False)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['author__username']

    def __str__(self):
        return 'Comentario Numero {}'.format(self.pk)


class Question(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length=200)
    description = models.TextField(verbose_name='Descripcion')
    language = models.CharField(verbose_name='Lenguaje', max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    created = models.DateTimeField(verbose_name='Fecha De Creacion:',auto_now_add=True, editable=False)
    comments = models.ManyToManyField(Comment,verbose_name='Comentarios')
    solved = models.BooleanField(default=False, verbose_name='Resuelto')

    def __str__(self):
        return self.title.capitalize()
