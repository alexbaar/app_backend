# Generated by Django 4.2.11 on 2024-05-03 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend_server', '0031_alter_workoutentry_session_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutentry',
            name='session_id',
        ),
        migrations.RemoveField(
            model_name='workoutentry',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='workouttype',
            name='id',
        ),
        migrations.AddField(
            model_name='workoutentry',
            name='email',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_server.myuser'),
        ),
        migrations.AlterField(
            model_name='workouttype',
            name='session_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
