# Generated by Django 2.1.7 on 2019-05-14 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generateletter', '0007_auto_20190514_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visaletters',
            name='Sex_1',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=100),
        ),
        migrations.AlterField(
            model_name='visaletters',
            name='Sex_2',
            field=models.CharField(blank=True, choices=[('M', 'M'), ('F', 'F')], max_length=100),
        ),
        migrations.AlterField(
            model_name='visaletters',
            name='Sex_3',
            field=models.CharField(blank=True, choices=[('M', 'M'), ('F', 'F')], max_length=100),
        ),
        migrations.AlterField(
            model_name='visaletters',
            name='Sex_4',
            field=models.CharField(blank=True, choices=[('M', 'M'), ('F', 'F')], max_length=100),
        ),
        migrations.AlterField(
            model_name='visaletters',
            name='Sex_5',
            field=models.CharField(blank=True, choices=[('M', 'M'), ('F', 'F')], max_length=100),
        ),
    ]
