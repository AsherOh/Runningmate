# Generated by Django 4.0.4 on 2022-06-30 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mateapp', '0003_post_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='writer',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]