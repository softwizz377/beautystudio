# Generated by Django 2.0 on 2020-05-07 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0012_auto_20200507_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='sentfile',
            field=models.FileField(default='', upload_to='resume/'),
        ),
    ]
