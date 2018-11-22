# Generated by Django 2.1.3 on 2018-11-22 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('founded_date', models.DateField()),
                ('buildings', models.ManyToManyField(related_name='companies', to='trading.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='trading.Building')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='trading.Company')),
                ('products', models.ManyToManyField(related_name='shops', to='trading.Product')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='companies', to='trading.Country'),
        ),
        migrations.AddField(
            model_name='company',
            name='employees',
            field=models.ManyToManyField(related_name='companies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='company',
            name='products',
            field=models.ManyToManyField(related_name='companies', to='trading.Product'),
        ),
        migrations.AddField(
            model_name='building',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='buildings', to='trading.Country'),
        ),
    ]