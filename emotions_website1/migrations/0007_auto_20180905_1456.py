# Generated by Django 2.1 on 2018-09-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emotions_website1', '0006_auto_20180905_1455'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VisitorResultEmotions',
        ),
        migrations.AddField(
            model_name='visitorqueryresult',
            name='face_rect',
            field=models.CharField(max_length=255, null=True, verbose_name='Face'),
        ),
    ]