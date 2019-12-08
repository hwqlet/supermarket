# Generated by Django 2.1.2 on 2019-12-08 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0017_auto_20191207_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('comment_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('shijian_comment', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='xiaofei',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='belong_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='supermarket.user'),
        ),
    ]
