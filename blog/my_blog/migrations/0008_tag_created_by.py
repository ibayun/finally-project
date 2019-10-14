# Generated by Django 2.2.6 on 2019-10-14 11:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_blog', '0007_auto_20191013_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete='CASCADE', to=settings.AUTH_USER_MODEL, verbose_name='user'),
            preserve_default=False,
        ),
    ]