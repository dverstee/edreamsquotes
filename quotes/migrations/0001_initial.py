# Generated by Django 2.0.4 on 2018-04-08 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_text', models.CharField(max_length=200)),
                ('quoter', models.CharField(max_length=200)),
                ('quotee', models.CharField(max_length=200)),
            ],
        ),
    ]
