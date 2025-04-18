from django.contrib import admin
from .models import (
    Director, Employee, News, Article,
    Infrastructure, Passport, Monitoring,
    Statistics, Center, Corruption, PhotoGallery, TelegramData
)

# Shared base class name updated for clarity
class BaseAdmin(admin.ModelAdmin):
    """Base admin class with default configuration (if needed in future)"""
    pass

# Statistics admin
@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ['s_employeements', 's_partners', 's_treateds']
    list_display_links = list_display
    list_filter = list_display


# Director admin
@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'p_number', 'email']
    search_fields = list_display
    list_display_links = list_display
    list_filter = ['full_name', 'p_number']


# Employee admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['emp_full_name', 'emp_speciality']
    search_fields = list_display
    list_display_links = list_display
    list_filter = list_display


# News admin
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['n_header', 'n_date', 'n_view_counter']
    search_fields = ['n_header']
    list_display_links = ['n_header', 'n_date']
    list_filter = ['n_header']


# Article admin
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['a_header', 'a_date', 'a_view_counter']
    search_fields = ['a_header']
    list_display_links = ['a_header', 'a_date']
    list_filter = ['a_header']


# Infrastructure admin
@admin.register(Infrastructure)
class InfrastructureAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']
    list_display_links = ['id', '__str__']
    # Consider customizing display fields if __str__ is not very descriptive


# Monitoring admin
@admin.register(Monitoring)
class MonitoringAdmin(admin.ModelAdmin):
    list_display = ['m_header', 'm_date', 'm_view_counter', 'status']
    search_fields = ['m_header', 'm_date', 'status']
    list_display_links = ['m_header', 'm_date', 'status']
    list_filter = ['m_header', 'm_date', 'status']
    ordering = ['-m_view_counter', 'm_date', 'status']


# Passport admin
@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ['p_fname', 'masked_p_code', 'given_date']
    search_fields = ['p_fname', 'p_code']
    list_display_links = ['p_fname', 'given_date']
    list_filter = ['given_date']
    ordering = ['p_fname', 'given_date']

    def masked_p_code(self, obj):
        """
        Mask the last 4 characters of the passport code for privacy.
        Example: AB123456 → AB12****
        """
        if obj.p_code and len(obj.p_code) >= 4:
            return obj.p_code[:-4] + "****"
        return obj.p_code

    masked_p_code.short_description = "Passport Code"


# Center admin - registered with default admin
admin.site.register(Center)
admin.site.register(TelegramData)
admin.site.register(Corruption)
admin.site.register(PhotoGallery)
