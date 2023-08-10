# Generated by Django 4.2 on 2023-08-08 03:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Bromine', '0005_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField(blank=True, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Bromine.mybloginfo')),
            ],
        ),
    ]
