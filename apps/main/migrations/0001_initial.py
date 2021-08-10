# Generated by Django 3.0.8 on 2021-08-09 11:57

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('text', models.CharField(max_length=200, null=True, verbose_name='Başlık')),
            ],
            options={
                'verbose_name': 'İçerik Tipleri',
                'verbose_name_plural': 'İçerik Tipleri Liste',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SiteMainSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('small_title', models.CharField(blank=True, max_length=120, null=True, verbose_name='Küçük Başlık')),
                ('main_title', models.CharField(blank=True, max_length=120, null=True, verbose_name='Ana Başlık')),
                ('button_title', models.CharField(blank=True, max_length=120, null=True, verbose_name='Buton Başlığı')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/contents/', verbose_name='Resim')),
                ('aligment', models.IntegerField(blank=True, null=True, verbose_name='Sıralama')),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Slider Liste',
                'ordering': ('aligment',),
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SiteMainWidgetsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('text', models.CharField(max_length=200, null=True, verbose_name='Başlık')),
            ],
            options={
                'verbose_name': 'Anasayfa Widget Tipi',
                'verbose_name_plural': 'Anasayfa Widget Tip Liste',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SiteSocialLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('facebook', models.URLField(blank=True, max_length=120, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, max_length=120, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, max_length=120, verbose_name='Instagram')),
                ('linkedin', models.URLField(blank=True, max_length=120, verbose_name='linkedin')),
                ('pinterest', models.URLField(blank=True, max_length=120, verbose_name='Pinterest')),
                ('youtube', models.URLField(blank=True, max_length=120, verbose_name='Youtube')),
                ('blog', models.URLField(blank=True, max_length=120, verbose_name='Blog')),
            ],
            options={
                'verbose_name': 'Site Sosyal Medya Hesapları',
                'verbose_name_plural': 'Site Sosyal Medya Hesapları Liste',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('header_text', models.CharField(blank=True, max_length=400, verbose_name='Firma Adı')),
                ('header_sort_text', models.CharField(blank=True, max_length=400, verbose_name='Başlık Metin')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Firma Açıklaması')),
                ('tag', models.TextField(blank=True, null=True, verbose_name='Head Tag')),
                ('footer_text', models.TextField(blank=True, null=True, verbose_name='Footer Metni')),
                ('company_logo', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='images/contents/', verbose_name='Firma Logosu')),
                ('company_logo_footer', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='images/contents/', verbose_name='Firma Logosu Footer')),
                ('keywords', models.TextField(blank=True, null=True, verbose_name='Etiketler')),
                ('bank_logo', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='images/contents/', verbose_name='Banka Logosu')),
                ('bank_name', models.TextField(blank=True, null=True, verbose_name='Banka Adı')),
                ('bank_iban', models.TextField(blank=True, null=True, verbose_name='IBAN')),
                ('bank_account_name', models.TextField(blank=True, null=True, verbose_name='Hesap Unvanı')),
                ('bank_info_message', models.TextField(blank=True, null=True, verbose_name='Ödeme Uyarı Metni')),
                ('phone', models.CharField(blank=True, max_length=200, verbose_name='Telefon')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='Adres')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-Posta')),
                ('company_about', ckeditor.fields.RichTextField(blank=True, verbose_name='Hakkımızda')),
                ('company_legal', ckeditor.fields.RichTextField(blank=True, verbose_name='Gizlilik Politikası')),
                ('company_faq', ckeditor.fields.RichTextField(blank=True, verbose_name='Sıkça Sorulan Sorular')),
                ('company_contact', ckeditor.fields.RichTextField(blank=True, verbose_name='İletişim')),
                ('company_legal_2', ckeditor.fields.RichTextField(blank=True, verbose_name='Teslimat ve İade')),
                ('company_legal_3', ckeditor.fields.RichTextField(blank=True, verbose_name='Mesafeli Satış Sözleşmesi')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='sites.Site', verbose_name='Firma')),
            ],
            options={
                'verbose_name': 'Site Ayarları',
                'verbose_name_plural': 'Site Ayarları Listesi',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SiteMainWidgets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('main_title', models.CharField(max_length=400, verbose_name='Başlık')),
                ('sub_text', models.CharField(blank=True, max_length=400, null=True, verbose_name='Alt Metin')),
                ('button_text', models.CharField(blank=True, max_length=400, null=True, verbose_name='Button Metni')),
                ('icon_class', models.CharField(blank=True, max_length=400, null=True, verbose_name='Icon Class')),
                ('url', models.CharField(blank=True, max_length=400, null=True, verbose_name='Link')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/contents/', verbose_name='Resim')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.SiteMainWidgetsType', verbose_name='İçerik Tipi')),
            ],
            options={
                'verbose_name': 'Anasayfa Widget',
                'verbose_name_plural': 'Anasayfa Widget Liste',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SiteContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('add_menu', models.BooleanField(blank=True, null=True, verbose_name='Menüye Ekle')),
                ('title', models.CharField(max_length=120, verbose_name='Başlık')),
                ('description', models.TextField(blank=True, verbose_name='Özet')),
                ('content', models.TextField(blank=True, verbose_name='İçerik')),
                ('url', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/contents/', verbose_name='Resim')),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.SiteContentType', verbose_name='İçerik Tipi')),
            ],
            options={
                'verbose_name': 'İçerikler',
                'verbose_name_plural': 'İçerikler Liste',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
    ]