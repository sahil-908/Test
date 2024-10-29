# # # from rest_framework import serializers
# # # from django.contrib.auth.models import User
# # # from .models import *

# # # # class StudentSerializer(serializers.ModelSerializer):
# # # #     class Meta:
# # # #         model = Student
# # # #         fields = "__all__"

# # # # class AttendanceSerializer(serializers.ModelSerializer):
# # # #     class Meta:
# # # #         model = Attendance
# # # #         fields = ['id', 'student', 'date', 'status']

# # # # class MarkAttendanceSerializer(serializers.Serializer):
# # # #     class_name = serializers.CharField(required=True)
# # # #     section = serializers.CharField(required=True)
# # # #     status = serializers.ChoiceField(choices=[('present', 'Present'), ('absent', 'Absent')], required=True)


# # # # class MarkBulkAttendanceSerializer(serializers.Serializer):
# # # #     class_name = serializers.CharField(required=True)
# # # #     section = serializers.CharField(required=True)
# # # #     student_ids = serializers.ListField(child=serializers.CharField(), required=True)
# # # #     status = serializers.ChoiceField(choices=[('present', 'Present'), ('absent', 'Absent')], required=True)




# # # class AttendanceSerializer(serializers.Serializer):
# # #     student_id = serializers.CharField(max_length=10)
# # #     status = serializers.ChoiceField(choices=[('Present', 'Present'), ('Absent', 'Absent')])

# # # class MarkAttendanceSerializer(serializers.Serializer):
# # #     date = serializers.DateField()
# # #     attendance = AttendanceSerializer(many=True)













# # from rest_framework import serializers
# # from django.contrib.auth.models import User
# # from .models import *

# # class TimetableSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Timetable
# #         fields = "__all__"




# # class SyllabusSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Syllabus
# #         fields = ['id', 'file', 'uploaded_at']

# # class SubjectSerializer(serializers.ModelSerializer):
# #     syllabus = serializers.ListField(child=serializers.FileField(),write_only=True)
# #     uploaded_files = SyllabusSerializer(many=True, read_only=True, source='syllabus')

# #     class Meta:
# #         model = Subject
# #         fields = "__all__"


# # class HobbiesSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Hobbies
# #         fields = "__all__"



# # #________________________________________________

# # class UserPermissionSerializer(serializers.Serializer):
# #     permissions = serializers.ListField(child=serializers.CharField())


# # class UserWithPermissionsSerializer(serializers.ModelSerializer):
# #     permissions = serializers.SerializerMethodField()

# #     class Meta:
# #         model = User
# #         fields = ['id', 'username', 'permissions']

# #     def get_permissions(self, obj):
# #         """
# #         Retrieves the codename of each permission assigned to the user.
# #         """
# #         return obj.user_permissions.values_list('codename', flat=True)





# # serializers.py

# # serializers.py

# from rest_framework import serializers
# from .models import *

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['id', 'name', 'email']


# class ExamTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ExamType
#         fields = ['id', 'name']


# class DateSheetSerializer(serializers.ModelSerializer):
#     exam_type = ExamTypeSerializer()

#     class Meta:
#         model = DateSheet
#         fields = ['id', 'subject', 'date', 'time', 'shift', 'exam_center', 'exam_type', 'exam_mode']


# class ResultSerializer(serializers.ModelSerializer):
#     student = StudentSerializer()

#     class Meta:
#         model = Result
#         fields = ['id', 'student', 'subject', 'marks_obtained', 'total_marks', 'exam_date', 'grade']



from rest_framework import serializers
from .models import *

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = "__all__"
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'date', 'event', 'status']










