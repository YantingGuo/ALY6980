# Generated by Django 2.1.15 on 2020-03-24 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagerecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(help_text='Enter a url that links to the article.', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Inforecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reported_label', models.TextField()),
                ('reported_label2', models.TextField()),
                ('location', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
