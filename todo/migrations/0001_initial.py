# Generated by Django 5.2.4 on 2025-07-12 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
