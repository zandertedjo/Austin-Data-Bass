# Generated by Django 3.0.4 on 2020-03-30 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0022_merge_20200330_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=105),
        ),
    ]
