# Generated by Django 4.2.7 on 2023-11-27 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_alter_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]