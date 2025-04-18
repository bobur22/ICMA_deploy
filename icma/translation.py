from modeltranslation.translator import register, TranslationOptions
from .models import News, Monitoring, Article, Director, Infrastructure, Employee, Center


@register(News)
class NewsTranslation(TranslationOptions):
    fields = ('n_header', 'n_paragraph',)


@register(Article)
class ArticleTranslation(TranslationOptions):
    fields = ('a_header', 'a_paragraph',)


@register(Director)
class DirectorTranslation(TranslationOptions):
    fields = ('full_name', 'biography', 'responsibility')


@register(Monitoring)
class MonitoringTranslation(TranslationOptions):
    fields = ('m_header', 'm_paragraph', )

@register(Infrastructure)
class InfrastructureTranslation(TranslationOptions):
    fields = ('inf_header', 'inf_paragraph',)

@register(Employee)
class EmployeeTranslation(TranslationOptions):
    fields = ('emp_full_name', 'emp_speciality',)

@register(Center)
class CenterTranslation(TranslationOptions):
    fields = ('c_header', 'c_paragraph',)
