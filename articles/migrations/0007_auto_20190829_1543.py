# Generated by Django 2.2.4 on 2019-08-29 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20190829_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment',
        ),
    ]
