# Generated by Django 4.1 on 2022-09-04 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_managers_user_date_joined_user_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.SmallIntegerField(default=None),
        ),
    ]