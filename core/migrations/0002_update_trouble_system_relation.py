# Generated by Django 2.0.2 on 2018-06-23 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_dtc_main_structure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trouble',
            name='system',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.System'),
        ),
    ]
