# Generated by Django 4.1.1 on 2022-11-03 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_areacultivo_apto_alter_areacultivo_disponivel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='areacultivo',
            old_name='apto',
            new_name='apta',
        ),
    ]