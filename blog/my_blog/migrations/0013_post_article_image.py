# Generated by Django 2.2.6 on 2019-10-15 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0012_auto_20191015_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='article_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/image/', verbose_name='image'),
        ),
    ]