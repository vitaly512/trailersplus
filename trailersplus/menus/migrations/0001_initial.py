# Generated by Django 3.0.8 on 2020-08-06 10:11

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menus', wagtail.core.fields.StreamField([('main_menu', wagtail.core.blocks.StructBlock([('menus', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('menu_title', wagtail.core.blocks.CharBlock()), ('menu_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('menu_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('special_class', wagtail.core.blocks.BooleanBlock(default=False, help_text='Special Class for PNG Image', required=False)), ('link_url', wagtail.core.blocks.PageChooserBlock(required=False))])))])))]))], blank=True, null=True)),
                ('menus_en', wagtail.core.fields.StreamField([('main_menu', wagtail.core.blocks.StructBlock([('menus', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('menu_title', wagtail.core.blocks.CharBlock()), ('menu_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('menu_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('special_class', wagtail.core.blocks.BooleanBlock(default=False, help_text='Special Class for PNG Image', required=False)), ('link_url', wagtail.core.blocks.PageChooserBlock(required=False))])))])))]))], blank=True, null=True)),
                ('menus_es', wagtail.core.fields.StreamField([('main_menu', wagtail.core.blocks.StructBlock([('menus', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('menu_title', wagtail.core.blocks.CharBlock()), ('menu_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('menu_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('special_class', wagtail.core.blocks.BooleanBlock(default=False, help_text='Special Class for PNG Image', required=False)), ('link_url', wagtail.core.blocks.PageChooserBlock(required=False))])))])))]))], blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_en', models.CharField(max_length=100, null=True)),
                ('title_es', models.CharField(max_length=100, null=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_title', wagtail.core.fields.RichTextField()),
                ('link_title_en', wagtail.core.fields.RichTextField(null=True)),
                ('link_title_es', wagtail.core.fields.RichTextField(null=True)),
                ('link_url', models.CharField(blank=True, max_length=500)),
                ('open_in_new_tab', models.BooleanField(blank=True, default=False)),
                ('link_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('link_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='menus.Menu')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
