# Generated by Django 4.2.1 on 2023-06-05 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_remove_eventdata_event_eventdata_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdata',
            name='type',
            field=models.IntegerField(choices=[(1, 'Event Name'), (2, 'Event Start Date'), (3, 'Event End Date'), (4, 'Application Start Date'), (5, 'Application End Date')], default=1),
            preserve_default=False,
        ),
    ]
