# Generated by Django 4.2 on 2023-04-17 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_certificado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificado',
            old_name='Certificado',
            new_name='certificado',
        ),
    ]
