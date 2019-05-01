# Generated by Django 2.1.7 on 2019-04-20 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightsbooking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='name',
            new_name='airport_name',
        ),
        migrations.AddField(
            model_name='destination',
            name='city_name',
            field=models.CharField(default='Belgrade', max_length=120),
            preserve_default=False,
        ),
    ]