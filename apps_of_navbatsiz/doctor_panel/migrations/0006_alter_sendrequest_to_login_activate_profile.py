# Generated by Django 4.2.2 on 2023-07-05 10:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doctor_panel", "0005_alter_sendrequest_to_login_activate_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sendrequest_to_login",
            name="activate_profile",
            field=models.CharField(
                choices=[(1, "yes"), (2, "no")],
                default=0,
                max_length=50,
                verbose_name="Activate Profile",
            ),
        ),
    ]
