# Generated by Django 4.0.6 on 2022-08-04 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_vendas_no_dia'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total_vendas',
            field=models.IntegerField(null=True),
        ),
    ]
