# Generated by Django 4.0.4 on 2022-07-09 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mateapp', '0002_alter_calendar_writer_alter_comment_user_and_more'),
        ('addproject', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='project',
            name='followers',
        ),
    ]
