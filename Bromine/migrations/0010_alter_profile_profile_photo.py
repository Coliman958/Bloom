# Generated by Django 4.2 on 2023-08-10 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bromine', '0009_alter_profile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
