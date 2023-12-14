# Generated by Django 4.2.3 on 2023-12-08 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catagory', '0002_alter_catagory_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('price', models.IntegerField()),
                ('images', models.ImageField(upload_to='photos/products')),
                ('stock', models.ImageField(upload_to='')),
                ('is_available', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catagory.catagory')),
            ],
        ),
    ]
