# Generated by Django 4.0.4 on 2022-05-16 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0008_alter_comment_author_alter_comment_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child', to='comments.comment'),
        ),
    ]
