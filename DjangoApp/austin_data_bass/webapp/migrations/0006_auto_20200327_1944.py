# Generated by Django 3.0.4 on 2020-03-27 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='imageURL',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='venue',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='venue',
            name='yelpURL',
            field=models.CharField(max_length=300),
        ),
    ]
