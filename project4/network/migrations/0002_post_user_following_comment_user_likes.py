# Generated by Django 4.1.4 on 2023-03-11 23:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(max_length=64)),
                ('body', models.TextField(max_length=300)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.today)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='users_followed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=200)),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing_comments', to='network.post')),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='user_likes', to='network.post'),
        ),
    ]
