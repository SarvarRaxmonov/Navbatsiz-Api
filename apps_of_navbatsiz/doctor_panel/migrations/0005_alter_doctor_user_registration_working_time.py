# Generated by Django 4.2.2 on 2023-07-06 16:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doctor_panel", "0004_doctor_user_registration_working_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor_user_registration",
            name="working_time",
            field=models.JSONField(default=dict, verbose_name="Working Time"),
        ),
    ]