# Generated by Django 3.2.9 on 2021-11-05 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cutter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='short_url',
            field=models.TextField(),
        ),
    ]
