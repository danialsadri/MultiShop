# Generated by Django 4.2.6 on 2023-10-27 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_color_options_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='text_en',
            field=models.TextField(max_length=500, null=True, verbose_name='text'),
        ),
        migrations.AddField(
            model_name='information',
            name='text_fa',
            field=models.TextField(max_length=500, null=True, verbose_name='text'),
        ),
    ]
