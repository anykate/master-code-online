from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator


# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.title)


pre_save.connect(slug_save, sender=Tutorial)
