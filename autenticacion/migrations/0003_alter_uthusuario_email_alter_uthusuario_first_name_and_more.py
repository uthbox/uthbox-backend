# Generated by Django 4.2 on 2023-04-05 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0002_alter_uthusuario_email_alter_uthusuario_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uthusuario',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='uthusuario',
            name='first_name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='uthusuario',
            name='last_name',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
