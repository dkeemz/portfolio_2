# Generated by Django 4.2.6 on 2023-11-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(default='Item Description', max_length=200)),
                ('live_link', models.CharField(blank=True, max_length=200, null=True)),
                ('github_link', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
