# Generated by Django 5.0 on 2024-11-22 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(max_length=50)),
                ('joined_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
