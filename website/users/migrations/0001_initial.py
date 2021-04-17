# Generated by Django 3.2 on 2021-04-17 09:49

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion
class Migration(migrations.Migration):

    initial = True
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hacker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('skill_1', models.CharField(max_length=100)),
                ('skill_2', models.CharField(max_length=100)),
                ('skill_3', models.CharField(max_length=100)),
            ],
        ),
    ]
