# Generated by Django 2.0 on 2020-05-15 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0015_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/'),
        ),
    ]