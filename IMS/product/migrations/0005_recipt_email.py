# Generated by Django 3.2 on 2021-08-09 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_recipt_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipt',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
