# Generated by Django 4.0.3 on 2022-05-10 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=200)),
                ('fName', models.CharField(max_length=200)),
                ('lName', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]
