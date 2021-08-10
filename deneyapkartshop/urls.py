from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth.views import LoginView

admin.site.site_header = 'Mağaza Yönetimi'
admin.site.index_title = 'Mağaza Yönetimi'
admin.site.site_title = 'Mağaza Yönetim Paneli'

from django.urls import include
from django.urls import path

from django.conf.urls import url
from django.contrib.auth import views

from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns

from apps.main.views import *


app_name = 'shop'

urlpatterns = i18n_patterns(

    path('shop/super/admin/', admin.site.urls),

    path('rosetta/', include("rosetta.urls")),

    path('', include(('apps.main.urls'), namespace='main')),




) + static(settings.STATIC_URL, document_root=settings.STATIC_URL) + static(settings.MEDIA_URL,
                                                                            document_root=settings.MEDIA_ROOT)
