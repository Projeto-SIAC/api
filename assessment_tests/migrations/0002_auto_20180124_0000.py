# Generated by Django 2.0.1 on 2018-01-24 00:00

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20180124_0000'),
        ('assessment_tests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='assessment_test',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='assessment_tests.AssessmentTest'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questions.Question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assessmenttest',
            name='archived_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assessmenttest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assessmenttest',
            name='created_by',
            field=models.CharField(default=datetime.datetime(2018, 1, 24, 0, 0, 14, 564510, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assessmenttest',
            name='questions',
            field=models.ManyToManyField(to='questions.Question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='assessmenttest',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]