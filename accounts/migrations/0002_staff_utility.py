# Generated by Django 3.1 on 2020-12-24 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('IT DEPT.', 'HR DEPT.'), ('FINANCE', 'AUDIT'), ('MARKETING', 'SALES')], max_length=100, null=True)),
                ('date_joined', models.DateField(max_length=200, null=True)),
                ('contact', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('aadhar_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='utility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('IsActive', 'IsNotActive')], max_length=100, null=True)),
            ],
        ),
    ]
