# Generated by Django 3.2.7 on 2021-09-24 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('express', '0002_auto_20210924_1207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientob',
            old_name='person',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='clientob',
            old_name='group',
            new_name='observ',
        ),
        migrations.RemoveField(
            model_name='client',
            name='observations',
        ),
        migrations.AddField(
            model_name='client',
            name='observations',
            field=models.ManyToManyField(through='express.ClientOb', to='express.Observ'),
        ),
    ]