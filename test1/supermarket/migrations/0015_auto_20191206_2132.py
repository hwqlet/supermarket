# Generated by Django 2.1.2 on 2019-12-06 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0014_auto_20191206_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dingdan',
            name='zhangdan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dingdans', to='supermarket.zhangdan'),
        ),
    ]
