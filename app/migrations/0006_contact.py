# Generated by Django 5.0 on 2024-11-22 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_frequentlyaskedquestion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('subject', models.CharField(max_length=255)),
                ('action_time', models.DateTimeField(blank=True, null=True)),
                ('is_success', models.BooleanField(default=False)),
                ('is_error', models.BooleanField(default=False)),
                ('error_message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
