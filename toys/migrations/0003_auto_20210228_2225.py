# Generated by Django 3.1.4 on 2021-02-28 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0002_auto_20210228_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='employee',
        ),
        migrations.AddField(
            model_name='company',
            name='employee',
            field=models.ManyToManyField(blank=True, null=True, related_name='company', to='toys.Employee'),
        ),
    ]
