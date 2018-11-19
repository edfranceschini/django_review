# Generated by Django 2.1.3 on 2018-11-19 02:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import review.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_date', models.DateTimeField(auto_created=True, verbose_name='Submission Date')),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
                ('rating', review.fields.IntegerRangeField(verbose_name='Rating')),
                ('summary', models.CharField(max_length=10240, verbose_name='Summary')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True, verbose_name='Sender IP')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.Company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Reviews',
                'verbose_name': 'Review',
            },
        ),
    ]
