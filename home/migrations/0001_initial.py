# Generated by Django 3.2.3 on 2021-10-14 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popular_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('image', models.ImageField(upload_to='photos/products')),
                ('image_havor', models.ImageField(upload_to='photos/products-havor')),
                ('stock', models.IntegerField()),
                ('new', models.BooleanField(default=False)),
                ('is_available', models.BooleanField(default=True)),
                ('date_joined_for_format', models.DateTimeField(auto_now_add=True)),
                ('last_login_for_format', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='For_You',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('image', models.ImageField(upload_to='photos/products')),
                ('image_havor', models.ImageField(upload_to='photos/products-havor')),
                ('stock', models.IntegerField()),
                ('new', models.BooleanField(default=False)),
                ('is_available', models.BooleanField(default=True)),
                ('date_joined_for_format', models.DateTimeField(auto_now_add=True)),
                ('last_login_for_format', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
    ]
