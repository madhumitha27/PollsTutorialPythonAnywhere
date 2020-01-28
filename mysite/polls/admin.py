from django.contrib import admin
from .models import Question,Choice


class AnserInLine(admin.TabularInline):
    model=Choice
    extra=3
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_txt','pub_date','was_published_recently')
    list_filter=['pub_date']
    search_fields = ['question_txt']
    fieldsets=[('Question Information',{'fields':['pub_date','question_txt']}),]
    inlines=[AnserInLine]
    def view_on_site(self,obj) :
        return "polls/index.html"

admin.site.register(Question,QuestionAdmin)
