# Generated by Django 4.1.4 on 2023-02-07 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_listing_bid_count_listing_current_winner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='body',
        ),
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(default='comment', max_length=64),
            preserve_default=False,
        ),
    ]
