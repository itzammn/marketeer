# Generated by Django 4.2.1 on 2023-05-23 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Campaigns', '0004_alter_lead_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subscriber',
            unique_together=set(),
        ),
    ]
