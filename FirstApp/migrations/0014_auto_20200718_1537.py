# Generated by Django 3.0.8 on 2020-07-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0013_auto_20200718_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selectfile',
            name='filename',
        ),
        migrations.AddField(
            model_name='selectfile',
            name='towhome',
            field=models.CharField(choices=[('vro', 'VRO'), ('vra', 'VRA'), ('ai', 'AI'), ('mro', 'MRO')], max_length=100, null=True),
        ),
    ]
