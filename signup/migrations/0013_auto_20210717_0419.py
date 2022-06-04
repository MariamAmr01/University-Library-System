# Generated by Django 3.2.5 on 2021-07-17 02:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('signup', '0012_alter_borrow_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='user',
            field=models.ForeignKey(default='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
