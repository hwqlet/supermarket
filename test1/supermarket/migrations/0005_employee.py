# Generated by Django 2.1.2 on 2019-12-03 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0004_auto_20191201_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_account', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('employee_password', models.CharField(max_length=20)),
                ('authority', models.CharField(max_length=4, null=True)),
            ],
        ),
    ]
