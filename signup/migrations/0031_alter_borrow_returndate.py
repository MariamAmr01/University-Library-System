# Generated by Django 3.2.5 on 2021-07-19 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0030_alter_borrow_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='returndate',
            field=models.DateField(default='datetime.date.today()'),
        ),
    ]
