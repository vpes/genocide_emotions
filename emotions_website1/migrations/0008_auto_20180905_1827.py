# Generated by Django 2.1 on 2018-09-05 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emotions_website1', '0007_auto_20180905_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitorqueryresult',
            name='index',
        ),
        migrations.AddField(
            model_name='visitorqueryresult',
            name='media_url',
            field=models.CharField(default='', max_length=512, verbose_name='Media url'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visitorqueryresult',
            name='proximity',
            field=models.FloatField(null=True, verbose_name='Proximity'),
        ),
        migrations.AddField(
            model_name='visitorqueryresult',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visitorqueryresult',
            name='url',
            field=models.CharField(default='', max_length=512, verbose_name='url'),
            preserve_default=False,
        ),
    ]
