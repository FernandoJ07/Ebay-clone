# Generated by Django 3.2.2 on 2021-06-19 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_comment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date',
        ),
    ]