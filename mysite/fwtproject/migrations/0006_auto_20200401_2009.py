# Generated by Django 3.0.3 on 2020-04-01 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fwtproject', '0005_tours_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='HowToReach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=50)),
                ('via', models.CharField(max_length=10)),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceToVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='tours',
            name='about',
            field=models.CharField(default=0, max_length=10000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tours',
            name='dn',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tours',
            name='sdesc',
            field=models.CharField(max_length=300),
        ),
    ]
