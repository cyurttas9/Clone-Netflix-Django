# Generated by Django 4.2.4 on 2023-09-26 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Kategori Adı')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='movie_pic')),
                ('video', models.FileField(upload_to='movie_video')),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('genre', models.ManyToManyField(to='movie.genre')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Filmler',
            },
        ),
    ]
