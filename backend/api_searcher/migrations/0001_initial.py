# Generated by Django 3.1.1 on 2020-12-18 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CWEDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CWEModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cwe_id', models.CharField(max_length=5)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CVEModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cve_id', models.CharField(max_length=17)),
                ('year', models.CharField(max_length=4)),
                ('month', models.CharField(max_length=2)),
                ('cwe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cwe_model', to='api_searcher.cwemodel')),
            ],
        ),
    ]
