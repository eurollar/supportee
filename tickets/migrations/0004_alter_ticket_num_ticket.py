# Generated by Django 4.0.4 on 2022-05-01 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_alter_ticket_num_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='num_ticket',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]