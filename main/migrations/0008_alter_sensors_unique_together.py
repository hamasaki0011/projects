# Generated by Django 3.2.17 on 2023-02-22 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_site_sensors_place'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sensors',
            unique_together={('place', 'device')},
        ),
    ]
