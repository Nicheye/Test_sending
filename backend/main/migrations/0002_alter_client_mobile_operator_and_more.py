# Generated by Django 4.2.6 on 2024-02-19 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='mobile_operator',
            field=models.CharField(choices=[('megafon', '926'), ('tele2', '900'), ('MTC', '982'), ('Ростелеком', '939'), ('Yota', '999')], max_length=20),
        ),
        migrations.AlterField(
            model_name='sender',
            name='mobile_operator',
            field=models.CharField(choices=[('megafon', '926'), ('tele2', '900'), ('MTC', '982'), ('Ростелеком', '939'), ('Yota', '999')], max_length=20),
        ),
    ]
