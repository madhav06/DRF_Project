# Generated by Django 3.1 on 2020-12-24 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField(max_length=100)),
                ('blood_group', models.CharField(max_length=200, null=True)),
                ('contact', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('aadhar_number', models.IntegerField()),
            ],
        ),
    ]
