# Generated by Django 3.1.7 on 2021-03-31 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image_link',
            field=models.CharField(max_length=2000000),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.CharField(max_length=2083),
        ),
    ]