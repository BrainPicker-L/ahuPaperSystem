# Generated by Django 2.0 on 2018-10-12 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_title', models.CharField(max_length=100, verbose_name='论文标题')),
                ('author', models.CharField(max_length=30, verbose_name='作者')),
                ('publisher', models.CharField(max_length=50, verbose_name='出版社')),
                ('ISSN', models.CharField(max_length=50, verbose_name='ISSN')),
                ('publish_year', models.CharField(max_length=50, verbose_name='年份')),
                ('keywords', models.CharField(max_length=50, verbose_name='关键字')),
                ('paper_url', models.CharField(max_length=50, verbose_name='原文地址')),
            ],
        ),
        migrations.CreateModel(
            name='PaperType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='paper',
            name='paper_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tool.PaperType'),
        ),
    ]
