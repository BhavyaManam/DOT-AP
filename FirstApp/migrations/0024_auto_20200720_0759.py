# Generated by Django 3.0.8 on 2020-07-20 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0023_auto_20200719_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectfile',
            name='towhom',
            field=models.CharField(choices=[('srinu1234', 'srinu1234')], max_length=100, null=True),
        ),
    ]
