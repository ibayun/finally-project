# Generated by Django 2.2.6 on 2019-10-15 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0011_auto_20191014_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]