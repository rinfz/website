# Generated by Django 2.0.7 on 2018-07-21 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180721_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listitem',
            name='style',
            field=models.TextField(blank=True, help_text='One style per line'),
        ),
        migrations.AlterField(
            model_name='section',
            name='tagline',
            field=models.CharField(blank=True, max_length=280),
        ),
    ]
