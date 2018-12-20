# Generated by Django 2.1.4 on 2018-12-16 21:24

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('patient', models.BooleanField(default=False)),
                ('medical', models.BooleanField(default=False)),
                ('gender', models.CharField(max_length=6)),
                ('age', models.IntegerField(default=0)),
                ('h', models.IntegerField(blank=True, default=0, null=True)),
                ('w', models.IntegerField(blank=True, default=0, null=True)),
                ('idd', models.IntegerField(blank=True, default=0, null=True)),
                ('station', models.BooleanField(blank=True, default=False)),
                ('derma', models.BooleanField(blank=True, default=False)),
                ('cpt', models.IntegerField(blank=True, null=True)),
                ('rbp', models.IntegerField(blank=True, null=True)),
                ('sc', models.IntegerField(blank=True, null=True)),
                ('fbs', models.IntegerField(blank=True, null=True)),
                ('rer', models.IntegerField(blank=True, null=True)),
                ('mhra', models.IntegerField(blank=True, null=True)),
                ('eia', models.IntegerField(blank=True, null=True)),
                ('oldpeak', models.IntegerField(blank=True, null=True)),
                ('sotp', models.IntegerField(blank=True, null=True)),
                ('nomv', models.IntegerField(blank=True, null=True)),
                ('thal', models.IntegerField(blank=True, null=True)),
                ('alarm', models.IntegerField(blank=True, default=0, null=True)),
                ('sex', models.BooleanField(blank=True, default=False)),
                ('risk', models.BooleanField(blank=True, default=False)),
                ('safe', models.BooleanField(blank=True, default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
