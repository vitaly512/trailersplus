# Generated by Django 3.0.9 on 2020-08-20 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200812_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='cart_title',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='header',
            name='checkout_button',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='header',
            name='item_added_text',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='header',
            name='remove_button',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
