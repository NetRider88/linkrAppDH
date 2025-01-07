# Generated by Django 5.1.3 on 2024-11-27 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "tracker",
            "0005_clickvariable_linkvariable_remove_customdomain_user_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="link",
            name="total_clicks",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="linkvariable",
            name="name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="linkvariable",
            name="placeholder",
            field=models.CharField(max_length=50),
        ),
    ]
