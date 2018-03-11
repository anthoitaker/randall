# Generated by Django 2.0.2 on 2018-03-11 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'causes',
                'ordering': ['description'],
                'verbose_name': 'cause',
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'solutions',
                'ordering': ['description'],
                'verbose_name': 'solution',
            },
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'symptoms',
                'ordering': ['description'],
                'verbose_name': 'symptom',
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'systems',
                'ordering': ['name'],
                'verbose_name': 'system',
            },
        ),
        migrations.CreateModel(
            name='Trouble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('code', models.CharField(max_length=5, unique=True, verbose_name='Code')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('original_title', models.CharField(max_length=200, verbose_name='Original Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('system', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.System')),
            ],
            options={
                'verbose_name_plural': 'troubles',
                'ordering': ['code'],
                'verbose_name': 'trouble',
            },
        ),
        migrations.AddField(
            model_name='symptom',
            name='trouble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Trouble'),
        ),
        migrations.AddField(
            model_name='solution',
            name='trouble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Trouble'),
        ),
        migrations.AddField(
            model_name='cause',
            name='trouble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Trouble'),
        ),
    ]
