# Generated by Django 4.0.4 on 2022-05-03 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_alter_ticket_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='num_ticket',
        ),
    ]
