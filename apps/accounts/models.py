import uuid
from django.contrib.postgres.fields import JSONField
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.db.models import Value, Q
from django.forms.models import model_to_dict
from django.utils import timezone
from django.utils.crypto import get_random_string

from django_countries.fields import CountryField, Country
from phonenumber_field.modelfields import PhoneNumber, PhoneNumberField

#from apps.accounts.validators import validate_possible_number
#from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group, User
from django.db.models import Q
class PossiblePhoneNumberField(PhoneNumberField):
    """Less strict field for phone numbers written to database."""

    #default_validators = [validate_possible_number]


class EmailPool(models.Model):
    text = models.CharField(max_length=256, blank=True, verbose_name=_('Mail'))

    def __str__(self):
        return self.text
    class Meta:
        ordering = ('text',)
        verbose_name = _('E-Mail')
        verbose_name_plural = _('E-Mail Liste')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))

class CityList(models.Model):
    name = models.CharField(max_length=256, blank=True, verbose_name=_('Şehir'))

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)
        verbose_name = _('Şehir')
        verbose_name_plural = _('Şehir Liste')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))

BOOL_CHOICES = ((True, 'Evet'), (False, 'Hayır'))
class Address(models.Model):
    name = models.CharField(max_length=256, blank=True, verbose_name=_('Adres İsmi'))
    first_name = models.CharField(max_length=256, verbose_name=_('Alıcı Ad'))
    last_name = models.CharField(max_length=256, verbose_name=_('Alıcı Soyad'))
    tc = models.BigIntegerField(blank=True,null=True,  verbose_name=_('TC veya Vergi Numarası'))
    company_name = models.CharField(max_length=256, blank=True,null=True, verbose_name=_('Şirket Adı ( Kurumsal Faturalar İçin )'))
    company_tax = models.CharField(max_length=256, blank=True, null=True,
                                   verbose_name=_('Vergi Dairesi( Kurumsal Faturalar İçin )'))
    street_address_1 = models.TextField(verbose_name=_('Adres'))
    city = models.ForeignKey(CityList, on_delete=models.CASCADE, verbose_name="Şehir")
    postal_code = models.CharField(max_length=20, blank=True, verbose_name=_('Posta Kodu'))
    phone = models.CharField(max_length=128, blank=True, default="", verbose_name=_('Telefon'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adres_user', verbose_name=_('Adres Sahibi'))
    billing_address = models.BooleanField(choices=BOOL_CHOICES, null=True, default=True,
                                          verbose_name=_('Fatura Adresi'))
    shipping_address = models.BooleanField(choices=BOOL_CHOICES, null=True, default=True,
                                           verbose_name=_('Teslimat Adresi'))
    class Meta:
        ordering = ("pk",)
        verbose_name = _('Adres')
        verbose_name_plural = _('Adresler')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))

    @property
    def summary(self):
        if self.billing_address == True:
            billing="Evet"
        else:
            billing = "Hayır"
        if self.shipping_address == True:
            shipping="Evet"
        else:
            shipping="Hayır"

        content = "<b>ADRES İSMİ:</b> %s <br><b>ALICI AD:</b> %s <br><b>ALICI SOYAD:</b> %s <br><b>TC VEYA VERGİ NUMARASI</b>  %s <br><b>ŞİRKET ADI ( KURUMSAL FATURALAR İÇİN ):</b>  %s <br><b>VERGİ DAİRESİ( KURUMSAL FATURALAR İÇİN ):</b>  %s <br><b>ADRES:</b>  %s <br><b>ŞEHİR:</b>  %s <br><b>POSTA KODU:</b>  %s <br><b>TELEFON:</b>  %s <br><b>FATURA ADRESİ:</b>  %s <br><b>TESLİMAT ADRESİ:</b>  %s " % (
        self.name, self.first_name, self.last_name, self.tc, self.company_name, self.company_tax, self.street_address_1,
        self.city, self.postal_code, self.phone, billing, shipping)
        return content

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        if self.billing_address == True:
            Address.objects.update(billing_address=False)
        if self.shipping_address == True:
            Address.objects.update(shipping_address=False)
        super(Address, self).save(*args, **kwargs)

    def __str__(self):
        if self.name:
            return "%s - %s" % (self.name, self.full_name)
        return self.full_name

    def __eq__(self, other):
        if not isinstance(other, Address):
            return False
        return self.as_data() == other.as_data()

    __hash__ = models.Model.__hash__

    def as_data(self):
        """Return the address as a dict suitable for passing as kwargs.
        Result does not contain the primary key or an associated user.
        """
        data = model_to_dict(self, exclude=["id", "user"])
        if isinstance(data["country"], Country):
            data["country"] = data["country"].code
        if isinstance(data["phone"], PhoneNumber):
            data["phone"] = data["phone"].as_e164
        return data

    def get_copy(self):
        """Return a new instance of the same address."""
        return Address.objects.create(**self.as_data())
