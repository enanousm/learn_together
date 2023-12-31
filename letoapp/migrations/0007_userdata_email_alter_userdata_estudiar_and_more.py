# Generated by Django 4.1.12 on 2023-10-31 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letoapp', '0006_userdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='email',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userdata',
            name='estudiar',
            field=models.CharField(default='MAT-021', max_length=7),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='first_name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='last_name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='username',
            field=models.CharField(max_length=25),
        ),
    ]
