# Generated by Django 2.2.5 on 2019-11-04 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generateletter', '0020_auto_20191104_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visaletters',
            name='Visa_Letter_N',
            field=models.CharField(default='<function Visaletters.number at 0x000001AAA0D89A68>', editable=False, max_length=200),
        ),
    ]
