# Generated by Django 3.0.3 on 2020-03-11 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageFilter', '0003_auto_20200307_0737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='GetImage',
        ),
    ]
