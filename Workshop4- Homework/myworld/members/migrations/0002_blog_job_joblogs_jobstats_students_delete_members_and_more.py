# Generated by Django 4.2.5 on 2023-09-26 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('release_date', models.DateTimeField(verbose_name='Realse Date')),
                ('blog_time', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=500)),
                ('start_date', models.DateTimeField(null=True, verbose_name='Blog start date')),
                ('end_date', models.DateTimeField(null=True, verbose_name='Blog end date')),
                ('start_no', models.IntegerField(null=True, verbose_name='No of blogs to skip')),
                ('no_of_blogs', models.IntegerField(null=True, verbose_name='No of blogs to extract')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Job created date')),
            ],
        ),
        migrations.CreateModel(
            name='JobLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.TextField(verbose_name='job logs')),
                ('function_name', models.TextField(verbose_name='Function name')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Log date')),
            ],
        ),
        migrations.CreateModel(
            name='JobStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('total_blogs', models.IntegerField(null=True, verbose_name='Total blogs found')),
                ('no_of_blogs_extracted', models.IntegerField(null=True, verbose_name='No of blogs extracted')),
                ('start_date', models.DateTimeField(null=True, verbose_name='Extraction start date')),
                ('end_date', models.DateTimeField(null=True, verbose_name='Extraction start date')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.job')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('roll_number', models.IntegerField()),
                ('mobile', models.CharField(max_length=10)),
                ('branch', models.CharField(choices=[('BA', 'BA'), ('B.COM', 'B.COM'), ('MBA', 'MBA'), ('CA', 'CA')], max_length=10, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Members',
        ),
        migrations.AddField(
            model_name='joblogs',
            name='job_stats',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.jobstats'),
        ),
    ]
