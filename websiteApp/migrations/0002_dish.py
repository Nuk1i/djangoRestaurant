# Generated by Django 3.1.5 on 2021-01-26 12:36

from django.db import migrations, models
import django.db.models.deletion
import websiteApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('is_visible', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=300, null=True)),
                ('photo', models.ImageField(upload_to=websiteApp.models.Dish.get_file_name_dishes)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websiteApp.category')),
            ],
        ),
    ]