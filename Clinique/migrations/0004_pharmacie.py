# Generated by Django 3.0.5 on 2021-05-12 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clinique', '0003_auto_20210422_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField(default=0)),
                ('latitude', models.FloatField(default=0)),
            ],
        ),
    ]
