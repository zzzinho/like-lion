# Generated by Django 2.2.10 on 2020-05-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jasoseol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
