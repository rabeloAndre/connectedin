# Generated by Django 3.1 on 2020-11-01 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfil', '0007_auto_20201030_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=255)),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postagem', to='perfil.perfil')),
            ],
            options={
                'ordering': ['-data_hora'],
            },
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='timeline', to='perfil.perfil')),
                ('postagem', models.ManyToManyField(to='timeline.Postagem')),
            ],
        ),
    ]