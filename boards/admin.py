from django.contrib import admin
from .models import Board,Topic
from django.contrib.auth.models import Group
# Register your models here.
admin.site.site_header='Boards Admin Panal'
admin.site.site_title='Boards Admin panal'

#من اجل اضافة توبيك بنفس مكان البورد يجب ان يكون في وسيط بهذه العملية وهذا الوسيط هو InlineTopic

#كلاس وسيط من اجل اضافة توبيك بنفس مكان اضافة بورد
class InlineTopic(admin.StackedInline):
        model =Topic
        extra=1


# كلاس خاص بالبورد يتم تعريف فيه كلاس اضافة توبيك
class BoardAdmin(admin.ModelAdmin):
        inlines=[InlineTopic]




#هذا الكلاس من اجل الخصائص الاساسية في الادمن بانيل 
class TopicAdmin(admin.ModelAdmin):
          fields=('subject','board','created_by','views')
          list_display=('subject','board','created_by','combine_subject_and_board')
          list_display_links=('board','created_by')
          list_editable = ('subject',)
          list_filter = ('created_by','board',)
          search_fields=('board','created_by',)
          # من اجل اضافة حقل جديد 
          def combine_subject_and_board(self,obj):
                  return f'{obj.subject} - {obj.board}'
                  
# بسبب وجود (بورد أدمن - التوبيك أدمن) تم استدعاء كل واحد لوحده لانو ديجانجو لاتتعرف عليه  
admin.site.register(Board,BoardAdmin)
admin.site.register(Topic,TopicAdmin)


