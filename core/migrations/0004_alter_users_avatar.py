# Generated by Django 4.1.1 on 2022-11-14 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_users_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='avatar',
            field=models.ImageField(blank=True, default='nulo', null=True, upload_to=''),
        ),
    ]