# # from django.contrib import admin
# # from .models import *

# # # admin.site.register(Student)
# # # admin.site.register(Attendance)


# # @admin.register(Student)
# # class StudentAdmin(admin.ModelAdmin):
# #     list_display = ('id', 'name', 'rollno', 'class_name', 'section')
# #     search_fields = ('name', 'rollno', 'class_name', 'section')
# #     list_filter = ('class_name', 'section')

# # @admin.register(Attendance)
# # class AttendanceAdmin(admin.ModelAdmin):
# #     list_display = ('student', 'status', 'date')
# #     search_fields = ('student__name', 'student__rollno')
# #     list_filter = ('status', 'date')



# # from django.contrib import admin
# # from .models import *

# # @admin.register(School)
# # class ClassAdmin(admin.ModelAdmin):
# #     list_display = ('name', 'school_code')
# #     search_fields = ('name', 'school_code')

# # @admin.register(Class)
# # class ClassAdmin(admin.ModelAdmin):
# #     list_display = ('name', 'section')
# #     search_fields = ('name', 'section')

# # @admin.register(Timetable)
# # class TimetableAdmin(admin.ModelAdmin):
# #     list_display = ('school_class', 'day', 'start_time', 'end_time', 'subject')
# #     list_filter = ('day', 'school_class')
# #     search_fields = ('subject', 'school_class__name')


from django.contrib import admin
from .models import Exam, Student, ExamType, Result

# Register Exam model with a custom display of fields
class ExamAdmin(admin.ModelAdmin):
    list_display = ('subject', 'student_class', 'date', 'time', 'examtype', 'mode', 'center')
    search_fields = ('subject', 'student_class', 'center')
    list_filter = ('student_class', 'date', 'examtype')

# Register Student model with a custom display of fields
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_class', 'roll_number')
    search_fields = ('name', 'roll_number')
    list_filter = ('student_class',)

# Register ExamType model
class ExamTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register Result model with a custom display of fields
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'marks_obtained', 'total_marks', 'grade')
    search_fields = ('student__name', 'exam__subject')
    list_filter = ('exam__student_class', 'grade')

# Register models with the custom admin classes
admin.site.register(Exam, ExamAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(ExamType, ExamTypeAdmin)
admin.site.register(Result, ResultAdmin)
