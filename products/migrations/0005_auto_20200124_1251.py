# Generated by Django 2.2.7 on 2020-01-24 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200124_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='products/%Y/%m/%d'),
        ),
    ]