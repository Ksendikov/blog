# Generated by Django 3.2.4 on 2021-07-20 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0003_auto_20210720_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]