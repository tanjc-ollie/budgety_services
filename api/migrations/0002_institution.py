# Generated by Django 5.1.4 on 2024-12-15 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitution_id', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'institution',
            },
        ),
    ]
