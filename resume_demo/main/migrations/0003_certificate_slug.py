# Generated by Django 5.1.4 on 2025-01-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_certificate_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
