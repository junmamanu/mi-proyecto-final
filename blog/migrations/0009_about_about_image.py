# Generated by Django 4.1.2 on 2022-11-19 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_about_alter_title_blog_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about_image',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]