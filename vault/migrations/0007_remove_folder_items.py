# Generated by Django 4.1.1 on 2022-09-19 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0006_alter_folder_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='items',
        ),
    ]