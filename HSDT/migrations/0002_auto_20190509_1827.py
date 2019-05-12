# Generated by Django 2.2 on 2019-05-09 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HSDT', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='description',
            field=models.CharField(default='', max_length=2000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='playerClass',
            field=models.CharField(choices=[(0, 'Druid'), (1, 'Hunter'), (2, 'Mage'), (3, 'Paladin'), (4, 'Priest'), (5, 'Rogue'), (6, 'Shaman'), (7, 'Warlock'), (8, 'Warrior'), (9, 'Dream'), (10, 'Neutral'), (None, '')], max_length=30, verbose_name='Player Class'),
        ),
        migrations.AlterField(
            model_name='deck',
            name='playerClass',
            field=models.CharField(choices=[(0, 'Druid'), (1, 'Hunter'), (2, 'Mage'), (3, 'Paladin'), (4, 'Priest'), (5, 'Rogue'), (6, 'Shaman'), (7, 'Warlock'), (8, 'Warrior'), (9, 'Dream'), (10, 'Neutral'), (None, '')], max_length=30, verbose_name='Player Class'),
        ),
    ]
