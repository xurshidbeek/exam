# Generated by Django 5.0.7 on 2024-07-21 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
