# Generated by Django 4.2.1 on 2023-08-15 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_comment_blog_comment_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
    ]