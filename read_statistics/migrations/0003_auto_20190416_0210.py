# Generated by Django 2.1.7 on 2019-04-15 18:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistics', '0002_readdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readdetail',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='readdetail',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='readnum',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType'),
        ),
    ]
