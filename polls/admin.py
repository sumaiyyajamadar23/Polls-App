from django.contrib import admin
from .models import Question,Choice
# Register your models here.
# admin.site.register(Question)
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Question',({'fields':['q_text']})),
        ('publication Date',({'fields':['pub_date']}))
    ]    
    inlines=[ChoiceInline]
    list_display=("q_text","pub_date","was_published_recently")
    list_filter=["pub_date"]
    search_fields=["q_text"]
admin.site.register(Question,QuestionAdmin)
