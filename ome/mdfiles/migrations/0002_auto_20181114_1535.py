# Generated by Django 2.1.3 on 2018-11-14 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdfiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='omefile',
            name='html_text',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='HTML yazı'),
        ),
        migrations.AlterField(
            model_name='omefile',
            name='markdown_text',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Markdown yazı'),
        ),
    ]
