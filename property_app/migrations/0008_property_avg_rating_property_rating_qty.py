# Generated by Django 4.0.4 on 2022-06-29 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_app', '0007_comment_user_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='property',
            name='rating_qty',
            field=models.IntegerField(default=0),
        ),
    ]
