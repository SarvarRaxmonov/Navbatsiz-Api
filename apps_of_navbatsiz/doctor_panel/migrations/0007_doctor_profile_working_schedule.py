# Generated by Django 4.2.1 on 2023-07-11 15:51

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doctor_panel", "0006_remove_doctor_profile_working_schedule"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor_profile",
            name="working_schedule",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=django.contrib.postgres.fields.ArrayField(
                    base_field=models.CharField(blank=True, max_length=30),
                    default=list,
                    size=10,
                ),
                default=list,
                size=10,
            ),
        ),
    ]