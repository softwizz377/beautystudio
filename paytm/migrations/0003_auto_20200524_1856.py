# Generated by Django 2.0 on 2020-05-24 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paytm', '0002_auto_20200523_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paytmhistory',
            name='BANKTXNID',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='BANK TXN ID'),
        ),
    ]
