# Generated by Django 3.1.1 on 2021-10-21 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0003_formdata_mailid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formdata',
            old_name='Problem',
            new_name='Problems',
        ),
    ]