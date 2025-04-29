from django.contrib import admin
from .models import QuestionCollection, Question, UserProgress

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

@admin.register(QuestionCollection)
class QuestionCollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'question_count')
    inlines = [QuestionInline]
    
    def question_count(self, obj):
        return obj.questions.count()
    question_count.short_description = 'Number of Questions'

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'collection', 'link')
    list_filter = ('collection',)
    search_fields = ('title',)

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'is_solved', 'review_count')
    list_filter = ('user', 'is_solved', 'question__collection')