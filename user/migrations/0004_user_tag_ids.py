# Generated by Django 4.2.6 on 2023-10-11 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        ('user', '0003_user_followings'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tag_ids',
            field=models.ManyToManyField(blank=True, related_name='user_tag', to='tag.tag'),
        ),
    ]
