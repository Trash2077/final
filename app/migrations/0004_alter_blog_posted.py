# Generated by Django 4.2.16 on 2024-11-27 22:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_blog_author_alter_blog_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 11, 28, 1, 15, 17, 999364), verbose_name='Опубликована'),
        ),
    ]
