# Generated by Django 4.1.3 on 2022-12-19 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_usersfiles_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='image')),
                ('username', models.CharField(max_length=150)),
                ('imagesize', models.CharField(max_length=100)),
            ],
        ),
    ]
