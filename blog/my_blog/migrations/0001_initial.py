# Generated by Django 2.2.6 on 2019-10-17 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_comments', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('article_text', models.TextField(blank=True, db_index=True)),
                ('article_date', models.DateTimeField(auto_now_add=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='image')),
            ],
            options={
                'ordering': ['-article_date'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_title', models.CharField(max_length=40, unique=True)),
                ('slug', models.SlugField(max_length=40, unique=True)),
                ('tag_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-tag_date'],
            },
        ),
    ]
