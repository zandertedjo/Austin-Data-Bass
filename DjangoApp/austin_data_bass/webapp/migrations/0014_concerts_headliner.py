# Generated by Django 2.2.11 on 2020-03-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_auto_20200329_0419'),
    ]

    operations = [
        migrations.AddField(
            model_name='concerts',
            name='headliner',
            field=models.CharField(default='', max_length=200),
        ),
    ]
