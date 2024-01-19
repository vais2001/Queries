# Generated by Django 4.2.9 on 2024-01-18 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('subjects', models.CharField(choices=[('HOME_SCIENCE', 'home_science'), ('MATHS', 'maths'), ('ENGLISH', 'english'), ('PHYSICS', 'physics'), ('COMPUTER', 'computer')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=200)),
                ('price', models.IntegerField(null=True)),
                ('published_date', models.DateField()),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='queries_app.student')),
            ],
        ),
    ]
