# Generated by Django 2.0 on 2020-05-23 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paytm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paytmhistory',
            name='TXNID',
            field=models.CharField(max_length=300, verbose_name='TXN ID'),
        ),
    ]