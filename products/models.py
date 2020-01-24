import random
import os
from django.db import models


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
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=9.99)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.name
