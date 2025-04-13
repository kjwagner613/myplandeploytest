# Generated by Django 5.2 on 2025-04-12 06:52

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MyPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2025, 1, 1))),
                ('physical', models.CharField(default='Body Plan', max_length=255)),
                ('spiritual', models.CharField(default='Spiritual Needs', max_length=255)),
                ('emotional', models.CharField(default='Emotional Needs', max_length=255)),
                ('mental', models.CharField(default='Support System', max_length=255)),
                ('quality', models.CharField(default='Fulfillment', max_length=255)),
                ('goals', models.CharField(default='Future Aspirations', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MealPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2025, 1, 1))),
                ('time_of_day', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Snack', 'Snack')], max_length=10)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylife.meal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
