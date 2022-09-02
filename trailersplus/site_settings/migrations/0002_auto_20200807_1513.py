# Generated by Django 3.0.8 on 2020-08-07 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailimages', '0022_uploadedimage'),
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='errorpage404',
            name='content',
        ),
        migrations.AddField(
            model_name='errorpage404',
            name='background_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='errorpage404',
            name='background_image_mobile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='errorpage404',
            name='button_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='errorpage404',
            name='button_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='errorpage404',
            name='button_text_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='errorpage404',
            name='button_text_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='errorpage404',
            name='sub_title',
            field=models.CharField(blank=True, max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='errorpage404',
            name='sub_title_en',
            field=models.CharField(blank=True, max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='errorpage404',
            name='sub_title_es',
            field=models.CharField(blank=True, max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='errorpage404',
            name='textarea',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='errorpage404',
            name='textarea_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='errorpage404',
            name='textarea_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='errorpage404',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='errorpage404',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='errorpage404',
            name='title_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]