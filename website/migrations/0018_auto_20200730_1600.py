# Generated by Django 3.0.8 on 2020-07-30 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_message'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='Contact',
        ),
    ]