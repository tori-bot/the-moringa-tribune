# Generated by Django 3.2 on 2022-05-27 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_article_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='code',
        ),
    ]
