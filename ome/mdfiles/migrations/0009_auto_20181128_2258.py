# Generated by Django 2.1.3 on 2018-11-28 19:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdfiles', '0008_auto_20181127_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='omefile',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='omefile',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=True, related_name='yazi', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
