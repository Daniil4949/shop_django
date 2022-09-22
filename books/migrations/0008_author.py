# Generated by Django 4.0.6 on 2022-09-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_cart_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('description', models.TextField()),
            ],
        ),
    ]