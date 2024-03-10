# Generated by Django 3.2.20 on 2024-03-06 20:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('author', models.CharField(default='Anonymous', max_length=250)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('body', models.TextField()),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]