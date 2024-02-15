# Generated by Django 4.2.7 on 2024-02-12 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movies_img'),
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movieitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wishlist.movie')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.movies')),
            ],
            options={
                'db_table': 'CartItem',
            },
        ),
    ]
