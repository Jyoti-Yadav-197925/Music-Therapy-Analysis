# Generated by Django 3.1.1 on 2021-10-21 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0006_auto_20211021_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='Symptoms',
            field=models.CharField(default='none', max_length=50),
        ),
    ]
