# Generated by Django 3.0.11 on 2021-03-11 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_auto_20210120_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='trailer',
            name='model',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
