# Generated by Django 4.1.3 on 2022-12-22 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_tasks_delete_todolist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('task', models.TextField()),
                ('description', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Tasks',
        ),
    ]
