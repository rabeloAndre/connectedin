# Generated by Django 3.1 on 2020-10-29 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_perfil_contatos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='convite',
            old_name='recebidos',
            new_name='convidado',
        ),
        migrations.RenameField(
            model_name='convite',
            old_name='solicitados',
            new_name='solicitante',
        ),
    ]
