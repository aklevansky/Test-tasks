# Generated by Django 2.1.1 on 2018-09-23 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fluffiness', models.IntegerField(choices=[(0, 'No fur'), (1, 'Short-haired'), (2, 'Medium-haired'), (4, 'Fluffy')], default=2)),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('breed', models.CharField(max_length=20)),
                ('breeder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
