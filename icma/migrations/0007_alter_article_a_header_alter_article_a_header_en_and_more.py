# Generated by Django 4.2.20 on 2025-04-21 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icma', '0006_alter_telegramdata_options_alter_news_n_header_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='a_header',
            field=models.CharField(help_text='Iltimos, maqola sarlavhasini kiriting.', max_length=220, verbose_name='maqola sarlavhasi'),
        ),
        migrations.AlterField(
            model_name='article',
            name='a_header_en',
            field=models.CharField(help_text='Iltimos, maqola sarlavhasini kiriting.', max_length=220, null=True, verbose_name='maqola sarlavhasi'),
        ),
        migrations.AlterField(
            model_name='article',
            name='a_header_ru',
            field=models.CharField(help_text='Iltimos, maqola sarlavhasini kiriting.', max_length=220, null=True, verbose_name='maqola sarlavhasi'),
        ),
        migrations.AlterField(
            model_name='article',
            name='a_header_uz',
            field=models.CharField(help_text='Iltimos, maqola sarlavhasini kiriting.', max_length=220, null=True, verbose_name='maqola sarlavhasi'),
        ),
        migrations.AlterField(
            model_name='news',
            name='n_header',
            field=models.CharField(help_text='Iltimos, yangilik sarlavhasini kiriting.', max_length=220, verbose_name='yangilik sarlavhasi'),
        ),
        migrations.AlterField(
            model_name='news',
            name='n_header_en',
            field=models.CharField(help_text='Iltimos, yangilik sarlavhasini kiriting.', max_length=220, null=True, verbose_name='yangilik sarlavhasi'),
        ),
        migrations.AlterField(
            model_name='news',
            name='n_header_ru',
            field=models.CharField(help_text='Iltimos, yangilik sarlavhasini kiriting.', max_length=220, null=True, verbose_name='yangilik sarlavhasi'),
        ),
        migrations.AlterField(
            model_name='news',
            name='n_header_uz',
            field=models.CharField(help_text='Iltimos, yangilik sarlavhasini kiriting.', max_length=220, null=True, verbose_name='yangilik sarlavhasi'),
        ),
    ]
