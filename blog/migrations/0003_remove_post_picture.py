# Generated by Django 2.1.9 on 2019-07-14 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='picture',
        ),
    ]