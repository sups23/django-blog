# Generated by Django 3.2.3 on 2021-05-27 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post/images', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Date'),
        ),
    ]
