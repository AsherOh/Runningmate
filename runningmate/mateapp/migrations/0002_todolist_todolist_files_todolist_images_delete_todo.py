# Generated by Django 4.0.4 on 2022-07-03 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mateapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='classname')),
                ('description', models.TextField(max_length=200, verbose_name='content')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='createday')),
                ('date_deadline', models.DateField(verbose_name='deadline')),
            ],
        ),
        migrations.CreateModel(
            name='TodoList_files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, upload_to='todo/files/%Y/%m')),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mateapp.todolist')),
            ],
        ),
        migrations.CreateModel(
            name='TodoList_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='todo/images/%Y/%m')),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mateapp.todolist')),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
