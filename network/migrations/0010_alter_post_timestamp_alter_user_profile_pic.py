# Generated by Django 4.2.5 on 2023-10-28 07:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("network", "0009_alter_user_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="timestamp",
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="profile_pic",
            field=models.ImageField(
                default="profile_pics/default.png", upload_to="profile_pics"
            ),
        ),
    ]
