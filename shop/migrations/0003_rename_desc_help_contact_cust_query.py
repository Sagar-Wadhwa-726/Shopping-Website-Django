# Generated by Django 4.0.4 on 2022-05-25 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_contact_desc_help'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='desc_help',
            new_name='cust_query',
        ),
    ]
