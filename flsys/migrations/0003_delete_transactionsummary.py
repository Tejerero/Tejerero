# Generated by Django 3.1.6 on 2022-06-30 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flsys', '0002_remove_transactionsummary_regid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TransactionSummary',
        ),
    ]
