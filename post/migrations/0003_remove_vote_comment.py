# Generated by Django 2.1.7 on 2019-03-05 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_vote_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='comment',
        ),
    ]