# Generated by Django 4.1.4 on 2023-02-04 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_alter_listing_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='users_watching', to='auctions.listing'),
        ),
    ]
