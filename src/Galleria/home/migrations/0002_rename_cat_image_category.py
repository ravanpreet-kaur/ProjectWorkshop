# Generated by Django 4.1.3 on 2022-11-08 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='cat',
            new_name='category',
        ),
    ]
