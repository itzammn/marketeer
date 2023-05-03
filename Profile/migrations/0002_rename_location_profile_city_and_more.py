# Generated by Django 4.1.7 on 2023-04-18 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='location',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='birthdate',
            new_name='dob',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='profile',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile/pics'),
        ),
    ]