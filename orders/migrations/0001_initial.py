# Generated by Django 3.1.4 on 2021-06-25 06:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import orders.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_auto_20210625_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=180)),
                ('address', models.CharField(max_length=180)),
                ('phone_number', models.CharField(max_length=10, validators=[orders.validators.validate_number])),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('completed', models.BooleanField(default=False)),
                ('date_ordered', models.DateField(default=datetime.datetime.now)),
                ('payment_method', models.CharField(choices=[('esewa', 'Esewa'), ('cod', 'Cash On Delivery')], default='cod', max_length=50)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('completed', models.BooleanField(default=False)),
                ('order_detail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='orders.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='products.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]