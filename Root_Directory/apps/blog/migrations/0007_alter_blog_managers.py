# Generated by Django 5.0 on 2023-12-14 09:06

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='blog',
            managers=[
                ('newmanager', django.db.models.manager.Manager()),
            ],
        ),
    ]
