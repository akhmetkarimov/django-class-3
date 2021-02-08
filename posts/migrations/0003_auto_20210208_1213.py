# Generated by Django 3.1.5 on 2021-02-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210204_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='posts', to='posts.Tag'),
        ),
    ]
