# Generated by Django 4.2.2 on 2023-07-04 15:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doctor_panel", "0003_alter_doctor_user_registration_working_days"),
    ]

    operations = [
        migrations.CreateModel(
            name="SendRequest_to_login",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("surname", models.CharField(max_length=50, verbose_name="Surename")),
                ("phone_number", models.IntegerField(verbose_name="Phone Number")),
                (
                    "scanned_document",
                    models.ImageField(
                        upload_to="images_of_sc_document",
                        verbose_name="Scanned Document",
                    ),
                ),
                (
                    "activate_profile",
                    models.CharField(
                        choices=[(1, "yes"), (2, "no")],
                        default=0,
                        max_length=50,
                        verbose_name="Activate Profile",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="doctor_user_registration",
            name="scanned_document",
        ),
    ]