# Generated by Django 2.1.2 on 2019-12-06 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0010_caigouyuan_employee_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='shouyinyuan',
            name='belong',
            field=models.ForeignKey(default='a_13013', on_delete=django.db.models.deletion.CASCADE, to='supermarket.liansuodian'),
            preserve_default=False,
        ),
    ]