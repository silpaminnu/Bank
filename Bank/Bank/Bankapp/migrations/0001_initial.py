# Generated by Django 4.1.5 on 2023-05-14 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('Age', models.IntegerField()),
                ('Phonenumber', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.TextField()),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('f', 'Female'), ('o', 'others')], max_length=100)),
                ('AccountType', models.CharField(choices=[('s', 'Savings account'), ('f', 'Fixed account'), ('sa', 'salary account'), ('c', 'current account'), ('n', 'NRI account'), ('r', 'reccuring deposit account')], max_length=100)),
                ('Branches', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bankapp.branches')),
                ('District', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bankapp.district')),
            ],
        ),
        migrations.AddField(
            model_name='Branches',
            name='District',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Bankapp.District'),
        ),
    ]
