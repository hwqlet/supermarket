# Generated by Django 2.1.2 on 2019-12-08 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0018_auto_20191208_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='xiaofei',
            field=models.FloatField(null=True),
        ),
    ]
