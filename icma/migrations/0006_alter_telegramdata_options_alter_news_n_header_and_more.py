# Generated by Django 4.2.20 on 2025-04-21 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icma', '0005_telegramdata'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='telegramdata',
            options={'verbose_name': 'TelegramData', 'verbose_name_plural': 'TelegramData'},
        ),
        migrations.AlterField(
            model_name='news',
            name='n_header',
            field=models.CharField(help_text='Iltimos, yangilik sarlavhasini kiriting.', max_length=80, verbose_name='yangilik sarlavhasi'),
        ),
        migrations.AlterField(
            model_name='news',
            name='n_header_en',
            field=models.CharField(help_text='Iltimos, yangilik sarlavhasini kiriting.', max_length=80, null=True, verbose_name='yangilik sarlavhasi'),
        ),
        migrations.AlterField(
            model_name='news',
            name='n_header_ru',
            field=models.CharField(help_text='Iltimos, yangilik sarlavhasini kiriting.', max_length=80, null=True, verbose_name='yangilik sarlavhasi'),
        ),
        migrations.AlterField(
            model_name='news',
            name='n_header_uz',
            field=models.CharField(help_text='Iltimos, yangilik sarlavhasini kiriting.', max_length=80, null=True, verbose_name='yangilik sarlavhasi'),
        ),
    ]
