# Generated by Django 3.0.8 on 2020-08-06 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagebazar', '0003_auto_20200806_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='Image',
            field=models.ImageField(upload_to='imagebazar/images/'),
        ),
    ]
