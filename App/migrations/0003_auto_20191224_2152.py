# Generated by Django 2.2.5 on 2019-12-24 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_article_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='a_title',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='comment',
            name='c_content',
            field=models.CharField(max_length=255),
        ),
    ]