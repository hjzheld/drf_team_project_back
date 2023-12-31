# Generated by Django 4.2.6 on 2023-10-06 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('nickname', models.CharField(max_length=100, unique=True)),
                ('mbti', models.CharField(blank=True, max_length=100, null=True)),
                ('blog', models.CharField(blank=True, max_length=100, null=True)),
                ('profile', models.ImageField(blank=True, upload_to='%Y/%m/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
