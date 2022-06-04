# Generated by Django 3.2.5 on 2021-07-15 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signup', '0006_delete_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=80)),
                ('ISBN', models.IntegerField()),
                ('period', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('year', models.IntegerField()),
            ],
        ),
    ]