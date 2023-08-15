# Generated by Django 4.2.4 on 2023-08-15 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0002_remove_collection_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='image',
            new_name='image_file',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='image_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]