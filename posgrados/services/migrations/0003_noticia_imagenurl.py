# Generated by Django 2.0.6 on 2018-09-12 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20180812_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='imagenUrl',
            field=models.TextField(blank=True),
        ),
    ]
