# Generated by Django 4.0 on 2022-02-08 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activity_type',
            field=models.CharField(choices=[('e', 'Event'), ('s', 'Saving')], default=None, max_length=1, null=True),
        ),
    ]
