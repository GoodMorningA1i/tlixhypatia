# Generated by Django 3.1.2 on 2020-11-13 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsummary', '0002_auto_20201112_0248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
            ],
        ),
    ]