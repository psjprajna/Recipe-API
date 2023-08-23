# Generated by Django 3.0.5 on 2020-07-14 21:41

from django.db import migrations
from django.db.migrations import RunPython


def delete_empty_categories(apps, schema):
    Category = apps.get_model("recipes", "Category")
    Category.objects.filter(type__isnull=True).delete()
    Category.objects.filter(type='').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0017_auto_20200713_1820'),
    ]

    operations = [
        RunPython(delete_empty_categories)
    ]
