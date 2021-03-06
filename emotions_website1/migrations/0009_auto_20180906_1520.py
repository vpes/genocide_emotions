# Generated by Django 2.1 on 2018-09-06 15:20

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('emotions_website1', '0008_auto_20180905_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitorqueryresult',
            name='original_path',
        ),
        migrations.AddField(
            model_name='visitorquery',
            name='max_proximity',
            field=models.FloatField(null=True, verbose_name='MaxProximity'),
        ),
        migrations.AddField(
            model_name='visitorquery',
            name='result_count',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='visitorqueryresult',
            name='emotions',
            field=jsonfield.fields.JSONField(default={}, verbose_name='Emotions'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='visitorqueryresult',
            name='face_rect',
            field=models.CharField(default='', max_length=255, verbose_name='Face'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='visitorqueryresult',
            name='image_path',
            field=models.CharField(default='', max_length=255, verbose_name='Image'),
            preserve_default=False,
        ),
    ]
