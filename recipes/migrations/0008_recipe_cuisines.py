# Generated by Django 3.0.5 on 2020-04-21 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_remove_recipe_cuisine'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cuisines',
            field=models.ManyToManyField(to='recipes.Cuisine'),
        ),
    ]
