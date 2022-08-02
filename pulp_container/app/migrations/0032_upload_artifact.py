# Generated by Django 3.2.13 on 2022-06-23 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0091_systemid'),
        ('container', '0031_replace_charf_with_textf'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='artifact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='uploads', to='core.artifact'),
        ),
    ]