# Generated by Django 4.1.1 on 2022-11-05 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areacultivo',
            name='disponivel',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
