from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    nome = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='media/',blank=True)

    class Meta:
        verbose_name = ("post")
        verbose_name_plural = ("posts")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("detalhar-post", kwargs={"pk": self.pk})

