# Generated by Django 4.2.7 on 2023-11-22 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='img',
            field=models.ImageField(default='anurag', upload_to='gallery'),
            preserve_default=False,
        ),
    ]