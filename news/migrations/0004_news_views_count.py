# Generated by Django 5.1.1 on 2024-10-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views_count',
            field=models.IntegerField(default=0),
        ),
    ]
