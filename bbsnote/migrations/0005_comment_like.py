# Generated by Django 4.1.7 on 2023-03-29 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbsnote', '0004_comment_author_comment_update_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
