# Generated by Django 3.0.14 on 2023-07-18 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='instargram/post/%Y/%m/%d'),
        ),
    ]