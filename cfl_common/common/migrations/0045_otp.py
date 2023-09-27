# Generated by Django 3.2.20 on 2023-09-27 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0044_update_activity_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='last_otp_for_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='otp_secret',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
