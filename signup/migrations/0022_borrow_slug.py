# Generated by Django 3.2.5 on 2021-07-17 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0021_alter_borrow_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
