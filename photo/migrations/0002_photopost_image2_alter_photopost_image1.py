# Generated by Django 4.1 on 2022-08-25 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("photo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="photopost",
            name="image2",
            field=models.ImageField(
                blank=True, null=True, upload_to="photos", verbose_name="イメージ2"
            ),
        ),
        migrations.AlterField(
            model_name="photopost",
            name="image1",
            field=models.ImageField(upload_to="photos", verbose_name="イメージ1"),
        ),
    ]
