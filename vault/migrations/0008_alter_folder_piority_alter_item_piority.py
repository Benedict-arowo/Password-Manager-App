# Generated by Django 4.1.1 on 2022-09-20 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0007_remove_folder_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='piority',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='piority',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]