# Generated by Django 3.0.2 on 2020-02-01 12:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookclub', '0002_book_copy_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена'),
            preserve_default=False,
        ),
    ]
