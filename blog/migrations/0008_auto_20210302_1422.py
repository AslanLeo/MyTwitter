# Generated by Django 2.1.2 on 2021-03-02 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210302_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_connected',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]