# Generated by Django 3.2.13 on 2022-05-17 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0002_auto_20220517_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=10)),
                ('inventory', models.ManyToManyField(to='logistics.Item')),
            ],
        ),
    ]
