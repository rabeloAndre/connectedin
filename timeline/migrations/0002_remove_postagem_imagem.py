# Generated by Django 3.1 on 2020-11-02 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postagem',
            name='imagem',
        ),
    ]
