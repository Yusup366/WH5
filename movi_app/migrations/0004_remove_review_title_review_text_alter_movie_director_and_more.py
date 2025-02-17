# Generated by Django 5.1.6 on 2025-02-17 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movi_app', '0003_rename_text_review_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
        migrations.AddField(
            model_name='review',
            name='text',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movi_app.director'),
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(blank=True, choices=[(1, '* '), (2, '* * '), (3, '* * * '), (4, '* * * * '), (5, '* * * * * ')], default=5, null=True),
        ),
    ]
