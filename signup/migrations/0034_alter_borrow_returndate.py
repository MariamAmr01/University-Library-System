# Generated by Django 3.2.5 on 2021-07-19 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0033_alter_borrow_returndate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='returndate',
            field=models.DateField(),
        ),
    ]
