# Generated by Django 3.2.9 on 2021-11-29 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0023_manifestsignature'),
    ]

    operations = [
        migrations.AddField(
            model_name='containerremote',
            name='sigstore',
            field=models.TextField(null=True),
        ),
    ]
