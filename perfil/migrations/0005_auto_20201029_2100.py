# Generated by Django 3.1 on 2020-10-30 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_auto_20201029_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='convite',
            old_name='convidado',
            new_name='recebidos',
        ),
        migrations.RenameField(
            model_name='convite',
            old_name='solicitante',
            new_name='solicitados',
        ),
    ]
