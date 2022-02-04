# Generated by Django 4.0.1 on 2022-01-29 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=70)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=70)),
                ('desc', models.CharField(default='', max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=90)),
                ('address', models.CharField(max_length=90)),
                ('address2', models.CharField(max_length=90)),
                ('city', models.CharField(max_length=90)),
                ('state', models.CharField(max_length=90)),
                ('zip_code', models.CharField(max_length=90)),
                ('phone', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
                ('category', models.CharField(default='', max_length=50)),
                ('sub_category', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
