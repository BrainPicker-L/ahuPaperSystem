# Generated by Django 2.0 on 2018-10-16 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='clicked_num',
            field=models.IntegerField(default=0),
        ),
    ]