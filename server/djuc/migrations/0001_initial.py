# Generated by Django 2.2.1 on 2019-09-13 22:28

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('notification_token', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PostSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('feed_url', models.CharField(max_length=2000)),
                ('auto_publish', models.BooleanField(default=False, help_text='Posts retrieved from this source get published automatically.')),
                ('auto_unpublish', models.BooleanField(default=True, help_text='Posts retrieved from this source get unpublished if removed from the source.')),
                ('auto_tags', models.ManyToManyField(blank=True, help_text='Tags to get applied automatically when retrieved.', to='djuc.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2000)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('link', models.CharField(max_length=2000, validators=[django.core.validators.RegexValidator('^https://.*$', 'The link should begin with https://')])),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('published', models.BooleanField(default=True)),
                ('external', models.BooleanField(default=False, help_text='Posts that are marked as external get updated if changes to             the source are made.')),
                ('external_id', models.CharField(max_length=255, null=True, unique=True)),
                ('external_source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='djuc.PostSource')),
                ('tags', models.ManyToManyField(blank=True, to='djuc.Tag')),
            ],
            options={
                'ordering': ['-date'],
                'permissions': [('can_publish', 'Publish/unpublish posts')],
            },
        ),
    ]
