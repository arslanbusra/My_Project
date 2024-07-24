# Generated by Django 5.0.6 on 2024-07-10 18:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=255)),
                ('authorname', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('booktype', models.CharField(choices=[('Edebiyat', 'Edebiyat'), ('Çocuk ve Gençlik', 'Çocuk ve Gençlik'), ('Eğitim ve Sınav', 'Eğitim ve Sınav'), ('Yabancı Dil', 'Yabancı Dil'), ('Araştırma Tarih', 'Araştırma Tarih'), ('Din ve Tasavvuf', 'Din ve Tasavvuf'), ('Sanat Tasarım', 'Sanat Tasarım'), ('Felsefe', 'Felsefe'), ('Hobi', 'Hobi'), ('Çizgi Roman', 'Çizgi Roman'), ('Bilim', 'Bilim'), ('Mizah', 'Mizah')], max_length=50)),
                ('booklang', models.CharField(choices=[('Türkçe', 'Türkçe'), ('İngilizce', 'İngilizce'), ('Almanca', 'Almanca'), ('Fransızca', 'Fransızca'), ('Diğer', 'Diğer')], max_length=50)),
                ('bookimage', models.ImageField(upload_to='book_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]