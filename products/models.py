import random
import os
from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator


def get_filename_extension(filepath):
    base_name = os.path.basename(filepath)
    ext = os.path.splitext(base_name)[1]
    return ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 12318351862358)
    ext = get_filename_extension(filename)
    final_filename = f"{new_filename}{ext}"
    return f"products/{new_filename}/{final_filename}"


class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=9.99)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)
