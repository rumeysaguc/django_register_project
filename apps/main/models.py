from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.sites.models import Site
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from apps.common.mixins.audit import AuditMixin
from apps.common.oneTextField.oneField import OneTextField
from versatileimagefield.fields import VersatileImageField
# Create your models here.

class SiteSettings(AuditMixin):
    site = models.OneToOneField(Site, related_name="settings", verbose_name=_('Firma'), on_delete=models.CASCADE)
    header_text = models.CharField(max_length=400, verbose_name=_('Firma Adı'), blank=True)
    header_sort_text = models.CharField(max_length=400, verbose_name=_('Başlık Metin'), blank=True)
    description = models.TextField(null=True, verbose_name=_('Firma Açıklaması'), blank=True)
    tag = models.TextField(null=True, verbose_name=_('Head Tag'), blank=True)
    footer_text = models.TextField(null=True, verbose_name=_('Footer Metni'), blank=True)
    company_logo = VersatileImageField(upload_to='images/contents/', null=True, verbose_name=_('Firma Logosu'),
                                     blank=True)
    company_logo_footer = VersatileImageField(upload_to='images/contents/', null=True, verbose_name=_('Firma Logosu Footer'),
                                     blank=True)
    keywords = models.TextField(null=True, verbose_name=_('Etiketler'), blank=True)
    bank_logo = VersatileImageField(upload_to='images/contents/', null=True,
                                              verbose_name=_('Banka Logosu'),
                                              blank=True)
    bank_name = models.TextField(null=True, verbose_name=_('Banka Adı'), blank=True)
    bank_iban = models.TextField(null=True, verbose_name=_('IBAN'), blank=True)
    bank_account_name = models.TextField(null=True, verbose_name=_('Hesap Unvanı'), blank=True)
    bank_info_message = models.TextField(null=True, verbose_name=_('Ödeme Uyarı Metni'), blank=True)
    phone = models.CharField(max_length=200,  blank=True,verbose_name=_('Telefon'))
    address = models.CharField(max_length=200,  blank=True,verbose_name=_('Adres'))
    email = models.EmailField(blank=True,verbose_name=_('E-Posta'))

    company_about = RichTextField(blank=True, verbose_name="Hakkımızda")
    company_legal = RichTextField(blank=True,verbose_name="Gizlilik Politikası")
    company_faq = RichTextField(blank=True, verbose_name="Sıkça Sorulan Sorular")
    company_contact = RichTextField(blank=True,verbose_name="İletişim")
    company_legal_2 = RichTextField(blank=True, verbose_name="Teslimat ve İade")
    company_legal_3 = RichTextField(blank=True, verbose_name="Mesafeli Satış Sözleşmesi")




    @property
    def image_url(self):
        if self.company_logo and hasattr(self.company_logo, 'url'):
            return self.company_logo.url

    @property
    def keywords_list(self):
        my_string = self.keywords
        keywords_list = [x.strip() for x in my_string.split(',')]

        return keywords_list

    def __str__(self) -> str:
        return self.header_text

    def save(self, *args, **kwargs):
        self.slug = slugify(self.header_text)
        super(SiteSettings, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Site Ayarları')
        verbose_name_plural = _('Site Ayarları Listesi')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class SiteSocialLinks(AuditMixin):
    facebook = models.URLField(max_length=120, blank=True, verbose_name=_('Facebook'))
    twitter = models.URLField(max_length=120, blank=True, verbose_name=_('Twitter'))
    instagram = models.URLField(max_length=120, blank=True, verbose_name=_('Instagram'))
    linkedin = models.URLField(max_length=120, blank=True, verbose_name=_('linkedin'))
    pinterest = models.URLField(max_length=120, blank=True, verbose_name=_('Pinterest'))
    youtube = models.URLField(max_length=120, blank=True, verbose_name=_('Youtube'))
    blog = models.URLField(max_length=120, blank=True, verbose_name=_('Blog'))

    class Meta:
        verbose_name = _('Site Sosyal Medya Hesapları')
        verbose_name_plural = _('Site Sosyal Medya Hesapları Liste')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))

class SiteContentType(OneTextField):
    class Meta:
        verbose_name = _('İçerik Tipleri')
        verbose_name_plural = _('İçerik Tipleri Liste')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))
class SiteContent(AuditMixin):
    type = models.ForeignKey(SiteContentType,on_delete=models.PROTECT, verbose_name=_("İçerik Tipi"))
    add_menu=models.BooleanField(blank=True,null=True,verbose_name=_('Menüye Ekle'))
    title = models.CharField(max_length=120, verbose_name=_('Başlık'))
    description = models.TextField(blank=True, verbose_name=_('Özet'))
    content = models.TextField(blank=True, verbose_name=_('İçerik'))
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='images/contents/', null=True, verbose_name=_('Resim'), blank=True)

    slug = models.SlugField(unique=True, editable=False)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SiteContent, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('İçerikler')
        verbose_name_plural = _('İçerikler Liste')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))



class SiteMainSlider(AuditMixin):
    small_title = models.CharField(max_length=120, null=True, blank=True, verbose_name=_('Küçük Başlık'))
    main_title = models.CharField(max_length=120, null=True, blank=True,verbose_name=_('Ana Başlık'))

    button_title = models.CharField(max_length=120, null=True, blank=True,verbose_name=_('Buton Başlığı'))


    url = models.URLField(null=True, blank=True, verbose_name=_('Link'))
    image = models.ImageField(upload_to='images/contents/', null=True, verbose_name=_('Resim'), blank=True)
    aligment = models.IntegerField(null=True, blank=True, verbose_name=_('Sıralama'))



    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url



    class Meta:
        ordering = ('aligment',)
        verbose_name = _('Slider')
        verbose_name_plural = _('Slider Liste')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))

class SiteMainWidgetsType(OneTextField):


    def __str__(self) -> str:
        return self.text


    class Meta:
        verbose_name = _('Anasayfa Widget Tipi')
        verbose_name_plural = _('Anasayfa Widget Tip Liste')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))

class SiteMainWidgets(AuditMixin):
    type = models.ForeignKey(SiteMainWidgetsType,on_delete=models.PROTECT, verbose_name=_("İçerik Tipi"))
    main_title = models.CharField(max_length=400, verbose_name=_('Başlık'))
    sub_text = models.CharField(max_length=400,null=True,blank=True, verbose_name=_('Alt Metin'))
    button_text = models.CharField(max_length=400,null=True,blank=True, verbose_name=_('Button Metni'))
    icon_class = models.CharField(max_length=400,null=True,blank=True, verbose_name=_('Icon Class'))
    url = models.CharField(max_length=400,null=True,blank=True, verbose_name=_('Link'))
    image = models.ImageField(upload_to='images/contents/', null=True, verbose_name=_('Resim'), blank=True)

    def __str__(self) -> str:
        return self.main_title


    class Meta:
        verbose_name = _('Anasayfa Widget')
        verbose_name_plural = _('Anasayfa Widget Liste')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))
