# Generated by Django 3.1.5 on 2021-01-30 13:50

from django.db import migrations, models
import websiteApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteApp', '0002_dish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('photo', models.ImageField(upload_to=websiteApp.models.Event.get_file_name_events)),
                ('event_date', models.DateField()),
                ('event_time', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
