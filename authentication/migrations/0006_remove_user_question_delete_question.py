# Generated by Django 4.1.1 on 2022-09-23 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_user_question_alter_question_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='question',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
