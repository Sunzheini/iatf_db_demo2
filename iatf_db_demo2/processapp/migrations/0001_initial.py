# Generated by Django 4.1.3 on 2022-11-02 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_name', models.CharField(max_length=30)),
                ('responsible', models.CharField(max_length=30)),
                ('evidence', models.CharField(max_length=30)),
            ],
        ),
    ]
