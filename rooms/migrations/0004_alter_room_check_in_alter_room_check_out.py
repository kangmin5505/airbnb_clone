# Generated by Django 4.0b1 on 2021-11-04 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_alter_room_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='check_in',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='check_out',
            field=models.TimeField(),
        ),
    ]
