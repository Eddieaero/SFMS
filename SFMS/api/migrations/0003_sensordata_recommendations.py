# Generated by Django 5.0.4 on 2024-05-04 15:14

import jsonfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_sensordata_air_humidity'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='recommendations',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]
