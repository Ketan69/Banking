# Generated by Django 4.0 on 2022-03-11 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_cust_passwd_alter_trans_receiver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trans',
            name='sender',
            field=models.IntegerField(default=0),
        ),
    ]
