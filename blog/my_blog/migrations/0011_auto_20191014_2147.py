# Generated by Django 2.2.6 on 2019-10-14 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0010_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
