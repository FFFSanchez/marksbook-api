# Generated by Django 4.2.4 on 2023-08-15 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0008_alter_bookmark_collection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='collection',
            new_name='collections',
        ),
    ]
