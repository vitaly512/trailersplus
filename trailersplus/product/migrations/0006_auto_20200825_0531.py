# Generated by Django 3.0.9 on 2020-08-25 05:31

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
#        ('wagtailmenus', '0024_auto_20201209_0039'),
        ('wagtailcore', '0052_pagelogentry'),
        ('product', '0005_auto_20200824_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpage',
            name='page_ptr',
        ),
        migrations.AlterModelOptions(
            name='categorymap',
            options={'ordering': ['order'], 'verbose_name': 'Category Map', 'verbose_name_plural': 'Category Maps'},
        ),
        migrations.RenameField(
            model_name='categoryfilter',
            old_name='filter_type',
            new_name='type',
        ),
        migrations.AddField(
            model_name='categorymap',
            name='order',
            field=models.IntegerField(default=1, verbose_name='Position in product list filter'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categorymap',
            name='translations',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='ProductList',
        ),
        migrations.DeleteModel(
            name='ProductPage',
        ),
    ]
