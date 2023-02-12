# Generated by Django 4.1.5 on 2023-02-11 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('desc', models.TextField(max_length=200)),
            ],
        ),
    ]