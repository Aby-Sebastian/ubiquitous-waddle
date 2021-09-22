# Generated by Django 3.2.7 on 2021-09-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=150)),
                ('short_url', models.CharField(max_length=20, unique=True)),
                ('clicks', models.PositiveIntegerField(blank=True, null=True)),
                ('total_clicks', models.IntegerField(blank=True, default=0, null=True)),
                ('titles', models.CharField(blank=True, default='No title found', max_length=200, null=True)),
            ],
        ),
    ]
