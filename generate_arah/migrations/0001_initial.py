# Generated by Django 3.2.8 on 2021-10-28 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('lokasi', models.CharField(max_length=2000)),
                ('sudut', models.CharField(max_length=2000)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
