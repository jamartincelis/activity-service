# Generated by Django 4.0 on 2022-03-03 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_alter_activity_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='payment',
            field=models.UUIDField(db_index=True, null=True),
        ),
    ]
