# Generated by Django 4.1 on 2023-12-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Census',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voting_id', models.IntegerField()),
                ('voter_id', models.IntegerField()),
            ],
        ),
    ]
