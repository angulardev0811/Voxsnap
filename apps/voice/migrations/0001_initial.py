# Generated by Django 2.2.4 on 2019-08-23 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_auto_20190821_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerVoiceName',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=120, unique=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='voicename', to='users.Customer')),
            ],
            options={
                'verbose_name': 'Customer Voice Name',
                'verbose_name_plural': 'Cutomer Voice Names',
            },
        ),
    ]
