# Generated by Django 5.0.4 on 2024-04-28 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensordata',
            name='id',
        ),
        migrations.AddField(
            model_name='sensordata',
            name='sensor_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
