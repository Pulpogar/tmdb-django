# Generated by Django 4.2.3 on 2023-07-14 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customMovies', '0003_rename_synopsis_movie_overview'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rate',
            field=models.FloatField(null=True),
        ),
    ]
