# Generated by Django 2.1.7 on 2019-06-07 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generateletter', '0009_auto_20190606_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visaletters',
            name='Organization',
        ),
    ]
