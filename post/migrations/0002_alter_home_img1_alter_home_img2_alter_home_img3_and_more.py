# Generated by Django 5.0.3 on 2024-05-13 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='img1',
            field=models.ImageField(blank=True, upload_to='logos/'),
        ),
        migrations.AlterField(
            model_name='home',
            name='img2',
            field=models.ImageField(blank=True, upload_to='logos/'),
        ),
        migrations.AlterField(
            model_name='home',
            name='img3',
            field=models.ImageField(blank=True, upload_to='logos/'),
        ),
        migrations.AlterField(
            model_name='home',
            name='img4',
            field=models.ImageField(blank=True, upload_to='logos/'),
        ),
    ]
