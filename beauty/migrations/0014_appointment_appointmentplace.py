# Generated by Django 2.0 on 2020-05-07 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0013_auto_20200507_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointmentplace',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
