# Generated by Django 3.0.8 on 2020-08-06 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagebazar', '0005_auto_20200806_1029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='Image',
            new_name='image',
        ),
    ]
