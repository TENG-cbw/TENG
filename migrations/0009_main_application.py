# Generated by Django 4.1 on 2023-05-31 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_01', '0008_structure'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='Application',
            field=models.CharField(default=1, max_length=64, verbose_name='Application'),
            preserve_default=False,
        ),
    ]
