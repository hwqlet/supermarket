# Generated by Django 2.1.2 on 2019-11-30 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0002_remove_shangpin_id_set_fenlei'),
    ]

    operations = [
        migrations.AddField(
            model_name='shangpin_id_set',
            name='is_sold',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
