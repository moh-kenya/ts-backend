# Generated by Django 4.2.4 on 2023-12-30 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0049_mapping_mappings_sort_weight_next'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='mapping',
            index=models.Index(condition=models.Q(('is_active', True), ('is_latest_version', True), models.Q(('id', models.F('versioned_object_id')), _negated=True)), fields=['versioned_object_id', '-created_at'], name='mappings_latest'),
        ),
    ]
