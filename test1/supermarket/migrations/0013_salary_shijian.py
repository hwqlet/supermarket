# Generated by Django 2.1.2 on 2019-12-06 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0012_caigouyuan_belong'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='shijian',
            field=models.DateField(null=True),
        ),
    ]
