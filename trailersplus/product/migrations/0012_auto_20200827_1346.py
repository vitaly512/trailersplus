# Generated by Django 3.0.9 on 2020-08-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_categoryfilter_field_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryfilter',
            name='field_name',
            field=models.CharField(choices=[('', '')], default='category__web_category__', max_length=25),
        ),
    ]
