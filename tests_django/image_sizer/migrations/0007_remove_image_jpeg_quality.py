# Generated by Django 2.0.4 on 2018-05-11 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_sizer', '0006_auto_20180510_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='jpeg_quality',
        ),
    ]