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


def index(request):
    newses = News.objects.all().order_by('-n_date')[:3]
    articles = Article.objects.all().order_by('-a_date')[:3]
    photo_gallery = PhotoGallery.objects.all()
    statistics = Statistics.objects.all()

    return render(request, template_name='index.html', context={'newses': newses,
                                                                'articles': articles
        , 'statistics': statistics, 'photo_gallery': photo_gallery})


def about_center(request):
    center = Center.objects.all()
    return render(request, template_name='about_center.html', context={'center': center})


def administrarion(request):
    director = Director.objects.all()
    return render(request, template_name='administration.html', context={'director': director})


def articles(request):
    paginator = Paginator(Article.objects.all().order_by('-a_date'), 9)
    page_number = request.GET.get("page")
    articles_obj = paginator.get_page(page_number)
    return render(request, template_name='articles.html', context={'articles_obj': articles_obj})


def articles_detail(request, id):
    articles = Article.objects.all().order_by('?')[:3]
    article = Article.objects.get(pk=id)

    article_count = get_object_or_404(Article, id=id)
    article_count.a_view_counter += 1
    article_count.save(update_fields=['a_view_counter'])
    return render(request, template_name='articles_detail.html', context={'articles': articles,
                                                                          'article': article,
                                                                          "article_count": article_count})


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
        html_content = render_to_string('email/email_en.html', {
            'name': contact.c_fname,
            'email': contact.c_email,
            'phone': contact.c_phone_number,
            'subject': contact.c_theme,
            'message': contact.c_message
        })

        # Send email
        send_mail(
            subject='Contact Form',
            message='Your message was confirmed.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[contact.c_email],
            html_message=html_content,
            fail_silently=False,
        )

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


def corruption(request):
    corruptions = Corruption.objects.all()
    return render(request, template_name='corruption.html', context={'corruptions': corruptions})


def employees(request):
    employees = Employee.objects.all()
    return render(request, template_name='employees.html', context={'employees': employees})


def infrostructure(request):
    infrostructure = Infrastructure.objects.all()
    return render(request, template_name='infrostructure.html', context={'infrostructure': infrostructure})


def monitoring(request):
    monitorings = Monitoring.objects.all().filter(status=1)
    return render(request, template_name='monitoring.html', context={'monitorings': monitorings})


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


def news(request):
    paginator = Paginator(News.objects.all().order_by('-n_date'), 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, template_name='news.html', context={'page_obj': page_obj})


def news_detail(request, id):
    newses = News.objects.all().order_by('?')[:3]
    news = News.objects.get(pk=id)
    news_count = get_object_or_404(News, id=id)
    news_count.n_view_counter += 1
    news_count.save(update_fields=['n_view_counter'])

    return render(request, template_name='news_detail.html', context={'newses': newses,
                                                                      'news': news,
                                                                      "news_count": news_count})


def hendling_404(request, exception):
    return render(request, "404.html")


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

def passport(request):
    return render(request, "page_development.html")
# def passport(request):
#     decision = 0
#     file_url = None
#     form = PassportForm()
#
#     if request.method == "POST":
#         form = PassportForm(request.POST, request.FILES)
#         code = request.POST.get("code", "").strip()
#         date = request.POST.get("date", "").strip()
#
#         if code and date:  # Bo‘sh qiymatlar tekshiriladi
#             if Passport.objects.filter(p_code=code, given_date=date).exists():
#                 decision = 1
#                 file_url = "/static/main/img/tuzilma.jpg"
#
#                 if form.is_valid():
#                     form.save()
#                     return redirect("master")
#             else:
#                 decision = -1  # Agar mos kelmasa, boshqa natija berish mumkin
#
#     return render(request, "passport.html", {"file_url": file_url, "decision": decision, "form": form})
