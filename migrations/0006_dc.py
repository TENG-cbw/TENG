# Generated by Django 4.1 on 2023-05-20 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_01', '0005_sl_alter_essay_mode_get_electrons_layer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ref_Publication_date', models.DateField(verbose_name='Ref.Publication date')),
                ('DOI', models.CharField(max_length=64, verbose_name='DOI')),
                ('img', models.FileField(max_length=128, upload_to='dc/', verbose_name='Image')),
            ],
        ),
    ]