# Generated by Django 3.0.4 on 2020-03-27 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_merge_20200327_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='topTracks',
        ),
        migrations.AddField(
            model_name='artist',
            name='spotifyLink',
            field=models.CharField(default='null', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='track1',
            field=models.CharField(default='null', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='track2',
            field=models.CharField(default='null', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='track3',
            field=models.CharField(default='null', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artist',
            name='bio',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='artist',
            name='imageLink',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='artist',
            name='spotifyID',
            field=models.CharField(max_length=50),
        ),
    ]
