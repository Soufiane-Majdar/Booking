# Generated by Django 4.0.3 on 2022-05-26 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_erreur'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='SuperAdmin',
        ),
    ]
