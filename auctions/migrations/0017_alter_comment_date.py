# Generated by Django 3.2.2 on 2021-06-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
