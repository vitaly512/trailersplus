# Generated by Django 3.0.10 on 2020-09-10 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0010_document_file_hash'),
        ('home', '0013_header_svg_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='svg_logo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document'),
        ),
    ]
