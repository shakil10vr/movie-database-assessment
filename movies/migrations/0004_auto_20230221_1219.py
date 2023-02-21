# Generated by Django 3.1.8 on 2023-02-21 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0003_auto_20230219_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_inappropriate',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='updated_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='rating',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(0, 'unresolved'), (1, 'inappropriate'), (2, 'close')], default=0)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marked', to='movies.movie')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]