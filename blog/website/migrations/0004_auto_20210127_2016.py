# Generated by Django 3.1.5 on 2021-01-27 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_post_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='approved',
            new_name='deleted',
        ),
    ]
