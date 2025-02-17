# Generated by Django 5.1.4 on 2025-01-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_certificate_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='description',
        ),
        migrations.AddField(
            model_name='certificate',
            name='tags',
            field=models.ManyToManyField(blank=True, to='main.tags'),
        ),
    ]
