# Import necessary Django modules for model creation and utilities
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .validators import validate_email, PhoneValidator, validate_f_name, valid_url_extension, validate_date
from django.utils import timezone
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField  # Used for rich text input in the admin

# Validator for passport field ensuring it contains exactly 7 alphanumeric characters
passport_validator = RegexValidator(
    regex=r'^[A-Za-z0-9]{7}$',
    message=_("Pasport raqami aniq 7 ta harf yoki raqamdan iborat bo‘lishi kerak."),
)


# Director model to store information about the organization's director
class Director(models.Model):
    full_name = models.CharField(max_length=50, verbose_name=_('toliq_ism'),
                                 help_text=_("Iltimos, rahbarning to‘liq ism-sharifini kiriting!"),
                                 validators=[validate_f_name])
    p_number = models.CharField(max_length=13,
                                validators=[PhoneValidator()],
                                verbose_name=_('telefon_raqam'),
                                help_text=_('Iltimos, direktorning telefon raqamini kiriting. Masalan: +998123456789'),
                                error_messages={'invalid': _('Iltimos, to‘g‘ri telefon raqamini kiriting!')}, )
    email = models.EmailField(verbose_name=_('pochta'),
                              help_text=_("Iltimos, Email manzilingizni kiriting."),
                              validators=[validate_email])
    biography = models.TextField(help_text=_("Iltimos, direktorning biografiyasini kiriting."),
                                 verbose_name=_("biografiya"), )
    responsibility = models.TextField(blank=True, null=True,
                                      verbose_name=_("majburiyati"),
                                      help_text=_("Iltimos, direktorning majburiyatlarini kiriting."))
    director_img = models.ImageField(upload_to='director/',
                                     verbose_name=_("rahbar_rasmi"),
                                     validators=[valid_url_extension],
                                     help_text=_(
                                         "Iltimos, direktorning fotosuratini yuklang (.jpg, .jpeg, .png formatlarida)!"))
    created_at = models.DateField(auto_now_add=True, verbose_name=_("yaratilgan vaqti"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("o'zgartirilgan vaqti"))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Direktor"
        verbose_name_plural = "Direktorlar"


# Employee model to store data about employees
class Employee(models.Model):
    emp_full_name = models.CharField(max_length=50, verbose_name=_('xodimning toliq ism'),
                                     help_text=_("Iltimos, xodimning to‘liq ismini kiriting."),
                                     validators=[validate_f_name])
    emp_speciality = models.CharField(max_length=50, verbose_name=_('xodimning mutaxassisligi'),
                                      help_text=_("Iltimos, xodimning mutaxassisligini kiriting."))
    employees_img = models.ImageField(upload_to='employee/', verbose_name=_('xodimning surati'),
                                      help_text=_(
                                          "Iltimos, xodimning fotosuratini yuklang (.jpg, .jpeg, .png formatlarida)!"),
                                      validators=[valid_url_extension])
    created_at = models.DateField(auto_now_add=True, verbose_name=_("yaratilgan vaqti"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("o'zgartirilgan vaqti"))

    def __str__(self):
        return self.emp_full_name

    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"


# News model for posting announcements or news
class News(models.Model):
    n_header = models.CharField(max_length=220, verbose_name=_("yangilik sarlavhasi"),
                                help_text=_("Iltimos, yangilik sarlavhasini kiriting."))
    n_paragraph = RichTextField(verbose_name=_("yangilik matni"), help_text=_("Iltimos, yangilik matnini kiriting."))
    n_date = models.DateField(default=timezone.now, verbose_name=_("yangilik sanasi"),
                              help_text=_("Iltimos, yangilik sanasini kiriting."))
    n_view_counter = models.PositiveIntegerField(default=0, verbose_name=_("yangilik ko'rishlar soni"))
    n_news_img = models.ImageField(upload_to='news/', verbose_name=_("yangilik rasmi"),
                                   help_text=_("Iltimos, fotosurat yuklang (.jpg, .jpeg, .png formatlarida)!"),
                                   validators=[valid_url_extension])
    created_at = models.DateField(auto_now_add=True, verbose_name=_("yaratilgan vaqti"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("o'zgartirilgan vaqti"))

    def __str__(self):
        return self.n_header

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"


# Article model for storing published articles
class Article(models.Model):
    a_header = models.CharField(max_length=220, verbose_name=_("maqola sarlavhasi"),
                                help_text=_("Iltimos, maqola sarlavhasini kiriting."))
    a_paragraph = RichTextField(verbose_name=_("maqola matni"),
                                help_text=_("Iltimos, maqola matnini kiriting."))
    a_date = models.DateField(default=timezone.now, verbose_name=_("maqola sanasi"),
                              help_text=_("Iltimos, maqola sanasini kiriting."))
    a_view_counter = models.IntegerField(default=0, verbose_name=_("maqola ko'rishlar soni"))
    a_article_img = models.ImageField(upload_to='article/', verbose_name=_("maqola rasmi"),
                                      help_text=_("Iltimos, rasm yuklang (.jpg, .jpeg, .png formatlarida)!"),
                                      validators=[valid_url_extension])
    created_at = models.DateField(auto_now_add=True, verbose_name=_("yaratilgan vaqti"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("o'zgartirilgan vaqti"))

    def __str__(self):
        return self.a_header

    class Meta:
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"


# Infrastructure model for showing center's facilities or services
class Infrastructure(models.Model):
    inf_img = models.ImageField(upload_to='infrostructure/', verbose_name=_("infroni surati"),
                                help_text=_("Iltimos, rasmingizni yuklang!"))
    inf_header = models.CharField(max_length=100, verbose_name=_("infrotuzilma sarlavhasi"),
                                  help_text=_("Iltimos, infrotuzilma sarlavhasini kiriting."), default=" ")
    inf_paragraph = models.TextField(verbose_name=_("infrotuzilma matni"),
                                     help_text=_("Iltimos, infrotuzilma matnini kiriting."), default=" ")
    created_at = models.DateField(auto_now_add=True, verbose_name=_("yaratilgan vaqti"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("o'zgartirilgan vaqti"))

    def __str__(self):
        return self.inf_img.name

    class Meta:
        verbose_name = "Infrostruktura"
        verbose_name_plural = "Infrostrukturalar"


# Monitoring model for reports or performance evaluations
class Monitoring(models.Model):
    ORDER_STATUS = ((0, 'Inactive'), (1, 'Active'))

    m_header = models.CharField(max_length=50, verbose_name=_("monitoring sarlavhasi"),
                                help_text=_("Iltimos, monitoring sarlavhasini kiriting."))
    m_paragraph = models.TextField(verbose_name=_("monitoring matni"),
                                   help_text=_("Iltimos, monitoring matnini kiriting."))
    m_date = models.DateField(default=timezone.now, verbose_name=_("monitoring sanasi"),
                              help_text=_("Iltimos, monitoring sanasini kiriting."))
    m_view_counter = models.IntegerField(default=0, verbose_name=_("monitoring ko'rishlar soni"))
    status = models.SmallIntegerField(choices=ORDER_STATUS, default=0, verbose_name=_("holati"),
                                      help_text=_("Iltimos, kartaning holatini kiriting."))
    m_img = models.ImageField(upload_to='monitoring/', verbose_name=_("monitoring rasmi"),
                              help_text=_("Iltimos, monitoring uchun rasm yuklang (.jpg, .jpeg, .png formatlarida)!"),
                              validators=[valid_url_extension])
    m_file = models.FileField(upload_to='monitoring/', verbose_name=_("monitoring fayli"),
                              help_text=_("Iltimos, faylingizni yuklang!"))
    created_at = models.DateField(auto_now_add=True, verbose_name=_("yaratilgan vaqti"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("o'zgartirilgan vaqti"))

    def __str__(self):
        return self.m_header

    class Meta:
        verbose_name = "Monitoring"
        verbose_name_plural = "Monitoringlar"


# Passport model for storing uploaded identification data
class Passport(models.Model):
    p_fname = models.CharField(max_length=50, verbose_name=_("Pasport egasining ismi"),
                               help_text=_("Iltimos, pasport egasining ismini kiriting."))
    p_code = models.CharField(max_length=7, verbose_name=_("Pasport kodi"),
                              help_text=_("Iltimos, pasport kodini kiriting."),
                              validators=[passport_validator])
    p_email = models.EmailField(verbose_name=_("Email manzili"),
                                help_text=_("Iltimos, email manzilingizni kiriting."),
                                validators=[validate_email])
    given_date = models.DateField(null=True, blank=True, default=timezone.now, verbose_name=_("Berilgan sana"),
                                  help_text=_("Iltimos, pasport berilgan sanani kiriting."),
                                  validators=[validate_date])
    p_img_upl = models.FileField(upload_to='passport/', verbose_name=_("Pasport rasmi"),
                                 help_text=_("Iltimos, pasport rasmini yuklang."))
    created_at = models.DateField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("O‘zgartirilgan vaqti"))

    def __str__(self):
        return self.p_fname

    class Meta:
        verbose_name = "Passport"
        verbose_name_plural = "Passportlar"


# Contact model for users to send messages or questions
class Contact(models.Model):
    c_fname = models.CharField(max_length=50, verbose_name=_("toliq ism"),
                               help_text=_("Iltimos, to‘liq ismingizni kiriting."))
    c_email = models.EmailField(verbose_name=_("pochta manzili"),
                                help_text=_("Iltimos, email manzilingizni kiriting."),
                                validators=[validate_email])
    c_phone_number = models.CharField(max_length=13, verbose_name=_("Telefon raqami"),
                                      help_text=_("Iltimos, telefon raqamingizni kiriting. Masalan: +998123456789"),
                                      error_messages={"invalid": _("Iltimos, to‘g‘ri telefon raqamini kiriting.")},
                                      validators=[PhoneValidator()])
    c_theme = models.CharField(null=True, blank=True, max_length=50, verbose_name=_("Mavzu"),
                               help_text=_("Iltimos, xabaringiz mavzusini kiriting."))
    c_message = models.TextField(null=True, blank=True, verbose_name=_("Xabar matni"),
                                 help_text=_("Iltimos, xabaringizni shu yerga yozing."))
    created_at = models.DateField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("O‘zgartirilgan vaqti"))

    def __str__(self):
        return self.c_fname

    class Meta:
        verbose_name = "Aloqa"
        verbose_name_plural = "Aloqalar"


# Statistics model for tracking key performance numbers
class Statistics(models.Model):
    s_employeements = models.PositiveIntegerField(verbose_name=_("statistika xodimlar"),
                                                  help_text=_("Iltimos, xodimlar sonini kiriting."))
    s_partners = models.PositiveIntegerField(verbose_name=_("statistika xamkorlar"),
                                             help_text=_("Iltimos, Xamkorlar sonini kiriting."))
    s_treateds = models.PositiveIntegerField(verbose_name=_("statistika davolanganlar"),
                                             help_text=_("Iltimos, Davolanganlar sonini kiriting."))
    created_at = models.DateField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("O‘zgartirilgan vaqti"))

    def __str__(self):
        return f"Xodimlar soni: {self.s_employeements}"

    class Meta:
        verbose_name = "Statistika"
        verbose_name_plural = "Statistikalar"


# Center model for displaying a center's description and images
class Center(models.Model):
    c_header = models.CharField(max_length=50, verbose_name=_("markaz sarlavhasi"),
                                help_text=_("Iltimos, markaz sarlavhasini kiriting."))
    c_paragraph = RichTextField(verbose_name=_("markaz matni"),
                                help_text=_("Iltimos, markaz matnini kiriting."))
    c_center_img_1 = models.ImageField(upload_to='center/', verbose_name=_("markaz rasmi"),
                                       help_text=_("Iltimos, rasm yuklang (.jpg, .jpeg, .png formatlarida)!"),
                                       validators=[valid_url_extension])
    c_center_img_2 = models.ImageField(upload_to='center/', verbose_name=_("markaz rasmi"),
                                       help_text=_("Iltimos, rasm yuklang (.jpg, .jpeg, .png formatlarida)!"),
                                       validators=[valid_url_extension])
    c_center_img_3 = models.ImageField(upload_to='center/', verbose_name=_("markaz rasmi"),
                                       help_text=_("Iltimos, rasm yuklang (.jpg, .jpeg, .png formatlarida)!"),
                                       validators=[valid_url_extension])
    created_at = models.DateField(auto_now_add=True, verbose_name=_("yaratilgan vaqti"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("o'zgartirilgan vaqti"))

    def __str__(self):
        return self.c_header

    class Meta:
        verbose_name = "Markaz"
        verbose_name_plural = "Markazlar"


# Corruption model for displaying a corruption related rules in one file
class Corruption(models.Model):
    c_corrupt_file = models.FileField(upload_to='korrupsiya/', verbose_name=_("korrupsiya fayli"),
                                      help_text=_("Iltimos, faylingizni yuklang!"), null=True, blank=True)

    created_at = models.DateField(auto_now_add=True, verbose_name=_("yaratilgan vaqti"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("o'zgartirilgan vaqti"))

    def __str__(self):
        return self.c_corrupt_file.name

    class Meta:
        verbose_name = "Korrupsiya"
        verbose_name_plural = "Korrupsiyalar"


# Photogallery model for displaying photos in index page.
class PhotoGallery(models.Model):
    photo = models.ImageField(
        upload_to='photogallery/',
        verbose_name=_("Gallereya rasmi"),
        help_text=_("Iltimos, rasm yuklang (.jpg, .jpeg, .png formatlarida)!"),
        validators=[valid_url_extension]
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name=_("Yaratilgan vaqti")
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name=_("O'zgartirilgan vaqti")
    )

    def __str__(self):
        return self.photo.name

    class Meta:
        verbose_name = _("Foto")
        verbose_name_plural = _("Fotolar")

class TelegramData(models.Model):
    chat_id = models.PositiveIntegerField()
    bot_token = models.CharField(max_length=46)

    def __str__(self):
        return f"{self.chat_id}"

    class Meta:
        verbose_name = "TelegramData"
        verbose_name_plural = "TelegramData"
