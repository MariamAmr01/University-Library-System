# Generated by Django 3.2.5 on 2021-07-14 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signup', '0002_auto_20210714_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
