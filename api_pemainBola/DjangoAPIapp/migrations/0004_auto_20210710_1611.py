# Generated by Django 3.2.5 on 2021-07-10 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoAPIapp', '0003_auto_20210709_2036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'ordering': ['-favorite_id']},
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='pemainbola',
            name='asalKlub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='klub', to='DjangoAPIapp.klub'),
        ),
    ]
