# Generated by Django 3.1.5 on 2021-04-10 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import userservices.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bills',
            fields=[
                ('patientemail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Accounts.authentication')),
                ('medicines_provided', models.BooleanField(default=False)),
                ('bill_status', models.BooleanField(default=False)),
                ('total_amount', models.FloatField(default=0.0)),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_bills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_status', models.BooleanField(default=False)),
                ('total_amount', models.FloatField(default=0.0)),
                ('date_generated', models.DateTimeField(auto_now_add=True)),
                ('patientemail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='opcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientname', models.CharField(max_length=100)),
                ('startdate', models.DateField(auto_now_add=True)),
                ('enddate', models.DateField(default=userservices.models.get_enddate)),
                ('disease', models.CharField(max_length=100)),
                ('temperature', models.FloatField(default=0)),
                ('is_assigned', models.BooleanField(default=False)),
                ('is_appointed', models.BooleanField(default=False)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('patientemail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='medicines_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_list', models.CharField(max_length=1024)),
                ('date_assigned', models.DateTimeField(auto_now_add=True)),
                ('patientemail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='medicines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=30)),
                ('medicine_quantity', models.IntegerField()),
                ('price', models.FloatField(default=0.0)),
                ('is_settled', models.BooleanField(default=False)),
                ('patientemail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
