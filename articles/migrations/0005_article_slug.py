# Generated by Django 5.1.4 on 2025-01-11 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]