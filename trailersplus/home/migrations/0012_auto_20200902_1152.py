# Generated by Django 3.0.9 on 2020-09-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20200831_0528'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='go_to_google_maps_en',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='header',
            name='go_to_google_maps_es',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
