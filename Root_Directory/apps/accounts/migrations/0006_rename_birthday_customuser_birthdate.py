# Generated by Django 5.0 on 2023-12-28 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customuser_profile_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='birthday',
            new_name='birthdate',
        ),
    ]
