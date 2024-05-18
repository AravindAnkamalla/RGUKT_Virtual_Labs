# Generated by Django 4.1.7 on 2023-07-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_res'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('sip', models.TextField()),
                ('sop', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='res',
            name='marks',
            field=models.IntegerField(null=True),
        ),
    ]
