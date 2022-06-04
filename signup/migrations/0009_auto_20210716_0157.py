# Generated by Django 3.2.5 on 2021-07-15 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0008_rename_status_book_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='period',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
