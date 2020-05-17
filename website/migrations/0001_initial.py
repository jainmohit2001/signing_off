# Generated by Django 3.0.6 on 2020-05-17 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('college_email', models.URLField(max_length=300)),
                ('form_donate', models.URLField(max_length=300)),
                ('form_receive', models.URLField(max_length=300)),
                ('college_ext', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
