# Generated by Django 4.1.1 on 2022-09-19 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0005_rename_pirority_folder_piority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
