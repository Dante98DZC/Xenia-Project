# Generated by Django 3.2.7 on 2021-10-02 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('express', '0007_alter_report_responce'),
    ]

    operations = [
        migrations.RenameField(
            model_name='executive',
            old_name='last_names',
            new_name='last_name',
        ),
    ]
