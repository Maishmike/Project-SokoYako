# Generated by Django 4.2.7 on 2023-11-25 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_category_cat_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(),
        ),
    ]