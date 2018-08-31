# Generated by Django 2.1 on 2018-08-31 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0001_initial'),
        ('robots', '0002_auto_20180822_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='robot',
            name='shipment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shipments.Shipment'),
        ),
    ]
