# Generated by Django 2.1.1 on 2018-10-02 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdfiles', '0002_auto_20181002_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
    ]