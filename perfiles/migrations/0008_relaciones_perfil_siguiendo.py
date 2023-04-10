# Generated by Django 4.2 on 2023-04-10 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfiles', '0007_perfil_verificado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario_seguido', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seguido', to=settings.AUTH_USER_MODEL)),
                ('usuario_siguiendo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='siguiendo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='perfil',
            name='siguiendo',
            field=models.ManyToManyField(blank=True, default=None, related_name='seguidos', through='perfiles.Relaciones', to='perfiles.perfil'),
        ),
    ]
