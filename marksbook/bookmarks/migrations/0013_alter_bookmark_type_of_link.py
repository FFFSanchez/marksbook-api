# Generated by Django 4.2.4 on 2023-08-15 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0012_alter_bookmark_options_alter_bookmark_type_of_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='type_of_link',
            field=models.CharField(choices=[('website', 'website'), ('book', 'book'), ('article', 'article'), ('music', 'music'), ('video', 'video')], default='website', verbose_name='type'),
        ),
    ]
