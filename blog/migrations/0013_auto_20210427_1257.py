# Generated by Django 2.1.2 on 2021-04-27 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210427_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_connected',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]