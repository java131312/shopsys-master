# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20160111_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\xbf\x80\xe6\xb4\xbb'),
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_description',
            field=models.CharField(help_text=b'meta\xe6\x8f\x8f\xe8\xbf\xb0', max_length=255, verbose_name=b'Meta \xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_keywords',
            field=models.CharField(help_text=b'meta\xe5\x85\xb3\xe9\x94\xae\xe8\xaf\x8d\xef\xbc\x8c\xe6\x9c\x89\xe5\x88\xa9\xe4\xba\x8eSEO\xef\xbc\x8c \xe7\x94\xa8\xe9\x80\x97\xe5\x8f\xb7\xe5\x88\x86\xe9\x9a\x94', max_length=255, verbose_name=b'Meta \xe5\x85\xb3\xe9\x94\xae\xe8\xaf\x8d'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text=b'\xe6\xa0\xb9\xe6\x8d\xaename\xe7\x94\x9f\xe6\x88\x90\xe7\x9a\x84\xef\xbc\x8c\xe7\x94\xa8\xe4\xba\x8e\xe7\x94\x9f\xe6\x88\x90\xe9\xa1\xb5\xe9\x9d\xa2URL\xef\xbc\x8c\xe5\xbf\x85\xe9\xa1\xbb\xe5\x94\xaf\xe4\xb8\x80', unique=True, verbose_name=b'Slug'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\x93\x81\xe7\x89\x8c'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=b'products', max_length=50, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name=b'\xe8\xae\xbe\xe4\xb8\xba\xe6\xbf\x80\xe6\xb4\xbb'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_bestseller',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\xa0\x87\xe4\xb8\xba\xe7\x95\x85\xe9\x94\x80'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\xa0\x87\xe4\xb8\xba\xe6\x8e\xa8\xe8\x8d\x90'),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_description',
            field=models.CharField(help_text=b'meta \xe6\x8f\x8f\xe8\xbf\xb0\xe6\xa0\x87\xe7\xad\xbe', max_length=255, verbose_name=b'Meta\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_keywords',
            field=models.CharField(help_text=b'meta \xe5\x85\xb3\xe9\x94\xae\xe8\xaf\x8d\xe6\xa0\x87\xe7\xad\xbe, \xe9\x80\x97\xe5\x8f\xb7\xe5\x88\x86\xe9\x9a\x94', max_length=255, verbose_name=b'Meta\xe5\x85\xb3\xe9\x94\xae\xe8\xaf\x8d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(unique=True, max_length=255, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(default=0.0, verbose_name=b'\xe6\x97\xa7\xe4\xbb\xb7\xe6\xa0\xbc', max_digits=9, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc', max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=50, verbose_name=b'\xe8\xae\xa1\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(help_text=b'\xe6\xa0\xb9\xe6\x8d\xaename\xe7\x94\x9f\xe6\x88\x90\xe7\x9a\x84\xef\xbc\x8c\xe7\x94\xa8\xe4\xba\x8e\xe7\x94\x9f\xe6\x88\x90\xe9\xa1\xb5\xe9\x9d\xa2URL\xef\xbc\x8c\xe5\xbf\x85\xe9\xa1\xbb\xe5\x94\xaf\xe4\xb8\x80', unique=True, max_length=255, verbose_name=b'Slug'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
