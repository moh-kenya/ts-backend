# Generated by Django 4.1.7 on 2023-04-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concepts', '0054_concept_concepts_retired_count_idx'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='concept',
            name='concepts_updated_6490d8_idx',
        ),
        migrations.RemoveIndex(
            model_name='concept',
            name='concepts_ver_sort_idx',
        ),
        migrations.RemoveIndex(
            model_name='concept',
            name='concepts_public_conditional',
        ),
        migrations.RemoveIndex(
            model_name='concept',
            name='concepts_ver_public',
        ),
        migrations.RemoveIndex(
            model_name='concept',
            name='concepts_all_for_count',
        ),
        migrations.RemoveIndex(
            model_name='concept',
            name='concepts_ver_for_count',
        ),
        migrations.RemoveIndex(
            model_name='concept',
            name='concepts_all_for_count2',
        ),
        migrations.RemoveIndex(
            model_name='concept',
            name='concepts_all_for_sort',
        ),
        migrations.RemoveIndex(
            model_name='concept',
            name='concepts_ver_for_sort',
        ),
        migrations.RemoveIndex(
            model_name='concept',
            name='concepts_ver_updated_idx',
        ),
        migrations.RemoveIndex(
            model_name='concept',
            name='concepts_ver_public_cond',
        ),
        migrations.RemoveIndex(
            model_name='concept',
            name='concepts_ver_all_for_count',
        ),
        migrations.RemoveIndex(
            model_name='concept',
            name='concepts_ver_all_for_sort',
        ),
        migrations.RemoveIndex(
            model_name='concept',
            name='concepts_ver_all_for_sort_2',
        ),
        migrations.RemoveIndex(
            model_name='concept',
            name='concepts_all_for_count3',
        ),
        migrations.RemoveIndex(
            model_name='concept',
            name='concepts_retired_count_idx',
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), models.Q(('public_access', 'None'), _negated=True)), fields=['-updated_at'], name='concepts_updated_6490d8_idx'),
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('is_latest_version', True), models.Q(('public_access', 'None'), _negated=True)), fields=['-updated_at'], name='concepts_ver_sort_idx'),
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('is_latest_version', True), models.Q(('public_access', 'None'), _negated=True)), fields=['public_access'], name='concepts_public_conditional'),
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), models.Q(('public_access', 'None'), _negated=True)), fields=['public_access'], name='concepts_ver_public'),
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('is_latest_version', True), models.Q(('public_access', 'None'), _negated=True)), fields=['parent_id'], name='concepts_public_cond'),
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('is_latest_version', True)), fields=['is_active'], name='concepts_all_for_count'),
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False)), fields=['is_active'], name='concepts_ver_for_count'),
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('is_latest_version', True)), fields=['parent_id'], name='concepts_all_for_count2'),
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('is_latest_version', True)), fields=['-updated_at'], name='concepts_all_for_sort'),
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False)), fields=['-updated_at'], name='concepts_ver_for_sort'),
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('id', models.F('versioned_object_id')), models.Q(('public_access', 'None'), _negated=True)), fields=['-updated_at'], name='concepts_ver_updated_idx'),
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('id', models.F('versioned_object_id')), models.Q(('public_access', 'None'), _negated=True)), fields=['public_access'], name='concepts_ver_public_cond'),
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('id', models.F('versioned_object_id')), models.Q(('public_access', 'None'), _negated=True)), fields=['parent_id'], name='concepts_ver_public_cond2'),
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('id', models.F('versioned_object_id'))), fields=['is_active'], name='concepts_ver_all_for_count'),
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('id', models.F('versioned_object_id'))), fields=['parent_id'], name='concepts_ver_all_for_count2'),
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('id', models.F('versioned_object_id'))), fields=['-updated_at'], name='concepts_ver_all_for_sort'),
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False)), fields=['-updated_at'], name='concepts_ver_all_for_sort_2'),
        ),
    ]
