# Generated by Django 2.1.1 on 2018-10-04 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConvertFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='files',
            name='convertfiles',
        ),
        migrations.AddField(
            model_name='convertfile',
            name='files',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mdfiles.Files', verbose_name='convertfile'),
        ),
    ]