# Generated by Django 4.0.4 on 2022-06-22 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_posts_postid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='rentfare',
            field=models.IntegerField(),
        ),
    ]
