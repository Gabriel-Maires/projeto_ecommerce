# Generated by Django 3.2.16 on 2022-10-14 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0003_remove_usuario_nome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='endereco',
            new_name='cep',
        ),
        migrations.AddField(
            model_name='usuario',
            name='numero',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
