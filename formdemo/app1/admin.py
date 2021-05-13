from django.contrib import admin

# Register your models here.

from .models import mcq_question,mcq_answer,true_false,true_false_answer

@admin.register(mcq_question)
class Mymodeladmin(admin.ModelAdmin):
    list_display = ['id','user','question','is_mcq_question']

@admin.register(mcq_answer)
class Mymodeladmin2(admin.ModelAdmin):
    list_display = ['id','user','question','answer'] 


@admin.register(true_false)
class Mymodeladmin3(admin.ModelAdmin):
    list_display = ['id','user','question']

@admin.register(true_false_answer)
class Mymodeladmin4(admin.ModelAdmin):
    list_display = ['id','user','question','answer']        


