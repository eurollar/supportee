# Generated by Django 4.0.4 on 2022-05-01 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='num_ticket',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]