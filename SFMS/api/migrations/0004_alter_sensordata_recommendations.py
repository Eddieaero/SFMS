# Generated by Django 5.0.4 on 2024-05-21 17:37

import jsonfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_sensordata_recommendations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='recommendations',
            field=jsonfield.fields.JSONField(blank=True, default=dict),
        ),
    ]
