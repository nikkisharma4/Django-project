# Generated by Django 3.1.7 on 2021-04-26 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210426_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallary',
            name='textpara',
            field=models.CharField(max_length=300),
        ),
    ]
