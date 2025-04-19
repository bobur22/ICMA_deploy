from django.shortcuts import render, redirect, get_object_or_404
from .models import News, Monitoring, Article, Director, Infrastructure, Employee, Passport, Contact, Statistics, \
    Center, Corruption, PhotoGallery, TelegramData
from django.template.loader import render_to_string
from .forms import PassportForm, ContactForm
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.translation import gettext_lazy as _
import requests

"""
    Index or Home Section:
"""


def index(request):
    newses = News.objects.all().order_by('-n_date')[:3]
    articles = Article.objects.all().order_by('-a_date')[:3]
    photo_gallery = PhotoGallery.objects.all()
    statistics = Statistics.objects.all()

    return render(request, template_name='index.html', context={'newses': newses,
                                                                'articles': articles
        , 'statistics': statistics, 'photo_gallery': photo_gallery})


"""
    About Section:
"""


def about_center(request):
    center = Center.objects.all()
    return render(request, template_name='about_center.html', context={'center': center})


"""
    Administration Section:
"""


def administration(request):
    director = Director.objects.all()
    return render(request, template_name='administration.html', context={'director': director})


"""
    Article Section:
"""


def articles(request):
    paginator = Paginator(Article.objects.all().order_by('-a_date'), 9)
    page_number = request.GET.get("page")
    articles_obj = paginator.get_page(page_number)
    return render(request, template_name='articles.html', context={'articles_obj': articles_obj})


"""
    Article detail Section:
"""


def articles_detail(request, id):
    articles = Article.objects.all().order_by('?')[:3]
    article = Article.objects.get(pk=id)

    article_count = get_object_or_404(Article, id=id)
    article_count.a_view_counter += 1
    article_count.save(update_fields=['a_view_counter'])
    return render(request, template_name='articles_detail.html', context={'articles': articles,
                                                                          'article': article,
                                                                          "article_count": article_count})


"""
    Contact us Section:
"""


def contact_us(request):
    telegram_data = TelegramData.objects.last()
    if request.method == "POST":
        # Get the POST data from the HTML form
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save the data to the model
        contact = Contact.objects.create(
            c_fname=name,
            c_email=email,
            c_phone_number=phone,
            c_theme=subject,
            c_message=message
        )

        # Prepare email content
        # html_content = render_to_string('email/email_en.html', {
        #     'name': contact.c_fname,
        #     'email': contact.c_email,
        #     'phone': contact.c_phone_number,
        #     'subject': contact.c_theme,
        #     'message': contact.c_message
        # })

        # Send email
        # send_mail(
        #     subject='Contact Form',
        #     message='Your message was confirmed.',
        #     from_email=settings.DEFAULT_FROM_EMAIL,
        #     recipient_list=[contact.c_email],
        #     html_message=html_content,
        #     fail_silently=False,
        # )

        # Send message to Telegram
        telegram_text = (
            "Contact Form to ICMA admins:\n"
            f"Full Name: {name}\n"
            f"Email: {email}\n"
            f"Phone number: {phone}\n"
            f"Subject: {subject}\n"
            f"Main message: {message}"
        )
        token = telegram_data.bot_token
        chat_id = telegram_data.chat_id
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        requests.get(url, params={'chat_id': chat_id, 'text': telegram_text})

        contact.delete()

        return redirect("contact_us")

    return render(request, 'contact_us.html')


"""
    Corruption Section:
"""


def corruption(request):
    corruptions = Corruption.objects.all()
    return render(request, template_name='corruption.html', context={'corruptions': corruptions})


"""
    Employees Section:
"""


def employees(request):
    employees = Employee.objects.all()
    return render(request, template_name='employees.html', context={'employees': employees})


"""
    Infrostructure Section:
"""


def infrostructure(request):
    infrostructure = Infrastructure.objects.all()
    return render(request, template_name='infrostructure.html', context={'infrostructure': infrostructure})


"""
    Monitoring Section:
"""


def monitoring(request):
    monitorings = Monitoring.objects.all().filter(status=1)
    return render(request, template_name='monitoring.html', context={'monitorings': monitorings})


"""
    Monitoring detail Section:
"""


def monitoring_detail(request, id):
    monitorings = Monitoring.objects.all().filter(status=1)
    monitoring_d = Monitoring.objects.get(pk=id)
    monitoring_count = get_object_or_404(Monitoring, id=id)

    # Increment the view counter
    monitoring_count.m_view_counter += 1
    monitoring_count.save(update_fields=['m_view_counter'])
    return render(request, template_name='monitoring_detail.html', context={'monitoring_d': monitoring_d,
                                                                            'monitorings': monitorings,
                                                                            "monitoring_count": monitoring_count})


"""
    News Section:
"""


def news(request):
    paginator = Paginator(News.objects.all().order_by('-n_date'), 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, template_name='news.html', context={'page_obj': page_obj})


"""
    News detail Section:
"""


def news_detail(request, id):
    newses = News.objects.all().order_by('?')[:3]
    news = News.objects.get(pk=id)
    news_count = get_object_or_404(News, id=id)
    news_count.n_view_counter += 1
    news_count.save(update_fields=['n_view_counter'])

    return render(request, template_name='news_detail.html', context={'newses': newses,
                                                                      'news': news,
                                                                      "news_count": news_count})


"""
    Handling 404 or Errors Section:
"""


def hendling_404(request, exception):
    return render(request, "404.html")


"""
    Passport Section:
    This section is currently under development.
    If needed, you can uncomment the next function to temporarily enable the working version of the passport page.
"""


def passport(request):
    return render(request, "page_development.html")

# def passport(request):
#     decision = 0
#     file_url = None
#     if request.method == "POST":
#         f_name = request.POST.get("f_name", "")
#         email = request.POST.get("email", "")
#         code = request.POST.get("code", "")
#         date = request.POST.get("date", "")
#         if Passport.objects.filter(p_code=code, date_of_birth=date).exists():
#             decision = 1
#             file_url = "/static/main/img/tuzilma.jpg"
#
#     return render(request, "passport.html", {"file_url": file_url, "decision": decision})
