# Generated by Django 3.1.8 on 2021-04-14 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0016_auto_20210402_0419'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='hierarchy_root',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='concepts.Concept'),
        ),
    ]
