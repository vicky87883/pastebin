# Generated by Django 5.1 on 2024-08-15 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textsnippet',
            name='language',
            field=models.CharField(choices=[('python', 'Python'), ('javascript', 'JavaScript'), ('html', 'HTML'), ('css', 'CSS')], default='python', max_length=20),
        ),
    ]
