# Generated by Django 4.0.4 on 2022-05-09 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='delete_flag',
            field=models.BooleanField(default=False),
        ),
    ]
