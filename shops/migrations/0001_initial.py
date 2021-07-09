# Generated by Django 3.1.4 on 2021-06-25 04:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('link', models.URLField(max_length=240)),
                ('image', models.ImageField(upload_to='banners/')),
                ('block', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('address', models.CharField(default='', max_length=100)),
                ('pan_number', models.CharField(default='', max_length=90)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='shops/')),
                ('slug', models.SlugField()),
                ('block', models.BooleanField(default=False)),
                ('hide', models.BooleanField(default=False)),
                ('is_trusted', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('limited', models.BooleanField(default=True)),
                ('date_added', models.DateField(default=django.utils.timezone.now, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='shops', to='shops.category')),
            ],
            options={
                'verbose_name_plural': 'Shops',
                'ordering': ('-id',),
            },
        ),
    ]
