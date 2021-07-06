
# django_register_project

Kayıt sayfası bootstrap ile oluşturuldu.
Veritabanı postgresql kullanıldı (pgadmin 4/ table_name= add_person)
Kullanıcı kaydı alındı. (Müdür, Öğretmen, Öğrenci selection ile sunuldu)
Postgresql veritabanında Person ismi ile bir table oluşturuldu.
Kayıtlar bu veritabanına eklendi.

Kayıt ol butonu home.html sayfasına yönlendirmesi yapıldı.
Home.html sayfasında bootstrap ile tabloda kişiler listelendi.


Veritabanı bilgileri aşağıdaki gibidir.
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql',

        'NAME': 'demo_test',

        'USER': 'postgres',

        'PASSWORD': '12345',

        'HOST': 'localhost',

        'PORT': '5432',

    }

}
