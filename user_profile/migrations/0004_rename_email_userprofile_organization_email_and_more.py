# Generated by Django 4.2.1 on 2023-06-09 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_userprofile_email_userprofile_logo_userprofile_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='email',
            new_name='organization_email',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='logo',
            new_name='organization_logo',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='phone',
            new_name='organization_phone',
        ),
    ]
