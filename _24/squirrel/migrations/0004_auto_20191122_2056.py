# Generated by Django 2.2.7 on 2019-11-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0003_auto_20191122_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='above_ground_sighter_measurement',
            field=models.BooleanField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='age',
            field=models.CharField(blank=True, default=None, max_length=8),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='chasing',
            field=models.BooleanField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='climbing',
            field=models.BooleanField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='color_notes',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='combination_of_primary_and_highlight_color',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='date',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='eating',
            field=models.BooleanField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='foraging',
            field=models.BooleanField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='hectare',
            field=models.CharField(blank=True, default=None, max_length=3),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='hectare_squirrel_number',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='highlight_fur_color',
            field=models.CharField(blank=True, default=None, max_length=8),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='kuks',
            field=models.BooleanField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='location',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='moans',
            field=models.BooleanField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='other_activities',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='primary_fur_color',
            field=models.CharField(blank=True, default=None, max_length=8),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='quaas',
            field=models.BooleanField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='running',
            field=models.BooleanField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='shift',
            field=models.CharField(blank=True, default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='specific_location',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='tail_flags',
            field=models.BooleanField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='tail_twitches',
            field=models.BooleanField(blank=True, default=None),
        ),
    ]
