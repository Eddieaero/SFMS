# Generated by Django 5.0.4 on 2024-04-28 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_sensordata_sensor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='sensor_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
