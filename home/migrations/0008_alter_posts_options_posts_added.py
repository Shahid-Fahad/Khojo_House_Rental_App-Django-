# Generated by Django 4.0.4 on 2022-06-23 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_posts_bathroom_alter_posts_bedroom'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-added']},
        ),
        migrations.AddField(
            model_name='posts',
            name='added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
