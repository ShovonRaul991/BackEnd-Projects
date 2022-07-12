# Generated by Django 4.0.6 on 2022-07-09 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='age',
            new_name='id',
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('priority', models.CharField(choices=[('L', 'Low'), ('M', 'MEDIUM'), ('H', 'HIGH')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.user')),
            ],
        ),
    ]
