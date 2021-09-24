# Generated by Django 3.2.5 on 2021-09-23 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('pfname', models.CharField(max_length=200)),
                ('plname', models.CharField(max_length=200)),
                ('pcollege', models.CharField(max_length=200)),
                ('pmobile', models.IntegerField()),
                ('page', models.IntegerField()),
            ],
        ),
    ]