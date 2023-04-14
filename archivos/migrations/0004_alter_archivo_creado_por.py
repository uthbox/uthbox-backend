# Generated by Django 4.2 on 2023-04-14 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('archivos', '0003_archivo_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='creado_por',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
