# Generated by Django 3.0.8 on 2020-07-07 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MOU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('dob', models.DateField(null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('image', models.ImageField(null=True, upload_to='profilepics/')),
                ('mailid', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]