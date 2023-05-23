# Generated by Django 4.2.1 on 2023-05-23 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Campaigns', '0005_alter_subscriber_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadconversion',
            name='campaign',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Campaigns.campaign'),
            preserve_default=False,
        ),
    ]