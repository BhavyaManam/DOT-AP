# Generated by Django 3.0.8 on 2020-07-18 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0012_auto_20200718_1328'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='adminfile',
            new_name='selectfile',
        ),
        migrations.DeleteModel(
            name='aplsafile',
        ),
        migrations.DeleteModel(
            name='compliancefile',
        ),
        migrations.DeleteModel(
            name='itfile',
        ),
        migrations.DeleteModel(
            name='ruralfile',
        ),
        migrations.DeleteModel(
            name='securityfile',
        ),
        migrations.DeleteModel(
            name='srfile',
        ),
        migrations.DeleteModel(
            name='technologyfile',
        ),
    ]