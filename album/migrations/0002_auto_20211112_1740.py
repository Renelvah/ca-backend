# Generated by Django 3.2.9 on 2021-11-12 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='package',
        ),
        migrations.DeleteModel(
            name='Package',
        ),
    ]
