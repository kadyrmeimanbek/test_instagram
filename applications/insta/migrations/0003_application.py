# Generated by Django 3.1.3 on 2020-11-11 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_instapost_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('check', models.BooleanField(default=False)),
            ],
        ),
    ]
