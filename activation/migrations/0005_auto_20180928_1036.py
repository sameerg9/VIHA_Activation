# Generated by Django 2.1.1 on 2018-09-28 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activation', '0004_activation_message_sent_success'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurse',
            name='phone_carrier',
            field=models.CharField(default='Telus', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nurse',
            name='phone_num',
            field=models.CharField(default='0000000000', max_length=12),
            preserve_default=False,
        ),
    ]
