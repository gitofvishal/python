# Generated by Django 4.1.1 on 2022-09-18 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='nlogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=122)),
                ('pas', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=122)),
            ],
        ),
    ]