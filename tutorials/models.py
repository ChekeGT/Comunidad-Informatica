from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
video_validator = FileExtensionValidator(['mp4','avi', 'webm'])



def image_custom_upload_to(instance, filename):
    return 'tutorials_images/' + filename


def video_custom_upload_to(instance, filename):
    return 'tutorials_videos/' + filename

class Tutorial(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    title = models.CharField(max_length=200, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', blank=True, null=True)
    language = models.CharField(verbose_name='Lenguaje', max_length=30, default='No especificado')
    video = models.FileField(null=True, blank=True, validators=[video_validator])
    created = models.DateTimeField(verbose_name='Fecha de Creacion:', auto_now_add=True, editable=False)
    updated = models.DateTimeField(verbose_name='Fecha De Edicion:', auto_now=True, editable=True)

    def __str__(self):
        return self.title
