# Generated by Django 3.1.4 on 2021-06-25 04:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('slug', models.SlugField(blank=True)),
                ('price', models.PositiveIntegerField()),
                ('discounted_from_price', models.PositiveIntegerField(blank=True, null=True)),
                ('sub_title', models.TextField(blank=True, max_length=300)),
                ('description', models.TextField(blank=True, max_length=3000)),
                ('main_image', models.ImageField(upload_to='products/')),
                ('image1', models.ImageField(blank=True, upload_to='products/')),
                ('image2', models.ImageField(blank=True, upload_to='products/')),
                ('image3', models.ImageField(blank=True, upload_to='products/')),
                ('image4', models.ImageField(blank=True, upload_to='products/')),
                ('in_stock', models.BooleanField(default=True)),
                ('sku', models.CharField(blank=True, max_length=50)),
                ('brand', models.CharField(blank=True, max_length=60)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('date_edited', models.DateField(auto_now=True)),
                ('featured', models.BooleanField(default=False)),
                ('block', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]