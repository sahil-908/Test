# # from django.db import transaction
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from .models import Timetable, Class
# # from .serializers import TimetableSerializer
# # from django.db import transaction
# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from .models import Timetable, Class
# # from .serializers import TimetableSerializer

# # class BulkTimetableView(APIView):
# #     def post(self, request):
# #         school_class_id = request.data.get('school_class')
        
# #         try:
# #             school_class = Class.objects.get(id=school_class_id)
# #         except Class.DoesNotExist:
# #             return Response({"error": "Class not found."}, status=status.HTTP_404_NOT_FOUND)
        
# #         timetable_data = request.data.get('timetables', [])
        
# #         if not timetable_data:
# #             return Response({"error": "No timetable entries provided."}, status=status.HTTP_400_BAD_REQUEST)

# #         response_messages = []
        
# #         for entry in timetable_data:
# #             entry['school_class'] = school_class.id
# #             day = entry.get('day')
# #             start_time = entry.get('start_time')
# #             end_time = entry.get('end_time')

# #             timetable_entry, created = Timetable.objects.get_or_create(
# #                 school_class=school_class,
# #                 day=day,
# #                 start_time=start_time,
# #                 end_time=end_time,
# #                 defaults={'subject': entry.get('subject')}  
# #             )

# #             if created:
# #                 response_messages.append(f"Created timetable for {day} from {start_time} to {end_time} in class {school_class.name}.")
# #             else:
# #                 timetable_entry.subject = entry.get('subject')  
# #                 timetable_entry.save()
# #                 response_messages.append(f"Updated timetable for {day} from {start_time} to {end_time} in class {school_class.name}.")

# #         return Response({"messages": response_messages}, status=status.HTTP_200_OK)

    
# #     def get(self, request):
# #         day = request.query_params.get('day', None)

# #         if day is None:
# #             return Response({"error": "Day parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

# #         timetables = Timetable.objects.filter(day=day)

# #         if not timetables.exists():
# #             return Response({"message": f"No timetable entries found for {day}."}, status=status.HTTP_404_NOT_FOUND)

# #         serializer = TimetableSerializer(timetables, many=True)

# #         return Response(serializer.data, status=status.HTTP_200_OK)



# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import generics, status
# from .serializers import SubjectSerializer
# from .models import *
# from .serializers import *

# class TimetableView(APIView):
#     def post(self, request):
#         # get data from user
#         school_class_id = request.data.get('school_class')
#         section = request.data.get('section')
#         school_code = request.data.get('school_code')

#         # verify the data
#         try:
#             school = School.objects.get(school_code=school_code)
#             school_class = Class.objects.get(id=school_class_id, section=section, school=school)  
#         except School.DoesNotExist:
#             return Response({"error": "School with the specified school code not found."}, status=status.HTTP_404_NOT_FOUND)
#         except Class.DoesNotExist:
#             return Response({"error": "Class with the specified section not found."}, status=status.HTTP_404_NOT_FOUND)

#         # Data entry
#         timetable_data = request.data.get('timetables', [])
        
#         if not timetable_data:
#             return Response({"error": "No timetable entries provided."}, status=status.HTTP_400_BAD_REQUEST)

#         response_messages = []
        
#         # Bulk data addition using for loop
#         for entry in timetable_data:
#             entry['school_class'] = school_class.id
#             day = entry.get('day')
#             start_time = entry.get('start_time')
#             end_time = entry.get('end_time')

#             timetable_entry, created = Timetable.objects.get_or_create(
#                 school_class=school_class,
#                 day=day,
#                 start_time=start_time,
#                 end_time=end_time,
#                 defaults={'subject': entry.get('subject')}  
#             )
#             # Update and create data according to if-else ladder
#             if created:
#                 response_messages.append(f"Created timetable for {day} from {start_time} to {end_time} in class {school_class.name} - {school_class.section}.")
#             else:
#                 timetable_entry.subject = entry.get('subject')  
#                 timetable_entry.save()
#                 response_messages.append(f"Updated timetable for {day} from {start_time} to {end_time} in class {school_class.name} - {school_class.section}.")

#         return Response({"messages": response_messages}, status=status.HTTP_200_OK)

#     def get(self, request):
#         # request data using query or json data
#         school_id = request.query_params.get('school_id')
        
#         school_class_id = request.data.get('school_class')
#         section = request.data.get('section')

#         # authenticate data
#         try:
#             school = School.objects.get(id=school_id)
#             school_class = Class.objects.get(id=school_class_id, section=section, school=school)
#         except School.DoesNotExist:
#             return Response({"error": "School with the specified ID not found."}, status=status.HTTP_404_NOT_FOUND)
#         except Class.DoesNotExist:
#             return Response({"error": "Class with the specified section not found."}, status=status.HTTP_404_NOT_FOUND)

#         timetables = Timetable.objects.filter(school_class=school_class)
#         #  query to add data in dict format
#         timetable_dict = {}
#         for timetable in timetables:
#             if timetable.day not in timetable_dict:
#                 timetable_dict[timetable.day] = []
            
#             timetable_dict[timetable.day].append({
#                 "start_time": timetable.start_time,
#                 "end_time": timetable.end_time,
#                 "subject": timetable.subject
#             })
#         #Return data
#         return Response({
#             "school_class": school_class.id,
#             "section": school_class.section,
#             "school_id": school.id,  
#             "timetables": timetable_dict
#         }, status=status.HTTP_200_OK)


# class SubjectUploadView(generics.GenericAPIView):
#     serializer_class = SubjectSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
        
#         subject_name = serializer.validated_data.get('name')
#         syllabus_files = serializer.validated_data.get('syllabus')
        

#         subject = Subject.objects.create(name=subject_name)
        
#         syllabi = []
#         for file in syllabus_files:
#             syllabus = Syllabus.objects.create(subject=subject, file=file)
#             syllabi.append(syllabus)
        
#         response_data = SubjectSerializer(subject).data
        
#         return Response(response_data, status=status.HTTP_201_CREATED)



# # from django.shortcuts import get_object_or_404


# # class HobbiesAPIView(APIView):

# #     def get(self, request, pk=None):
# #         if pk:
# #             user_profile = get_object_or_404(Hobbies, pk=pk)
# #             serializer = HobbiesSerializer(user_profile)
# #             return Response(serializer.data, status=status.HTTP_200_OK)
# #         else:
# #             user_profiles = Hobbies.objects.all()
# #             serializer = HobbiesSerializer(user_profiles, many=True)
# #             return Response(serializer.data, status=status.HTTP_200_OK)

# #     def post(self, request):
# #         serializer = HobbiesSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def patch(self, request, pk=None):
# #         if pk is None:
# #             return Response({"error": "Method PATCH not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# #         user_profile = get_object_or_404(Hobbies, pk=pk)
# #         serializer = HobbiesSerializer(user_profile, data=request.data, partial=True)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_200_OK)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def delete(self, request, pk=None):
# #         if pk is None:
# #             return Response({"error": "Method DELETE not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
# #         user_profile = get_object_or_404(Hobbies, pk=pk)
# #         user_profile.delete()
# #         return Response({"message": "Hobbies successfully deleted"},status=status.HTTP_204_NO_CONTENT)


# from django.contrib.auth.models import User, Permission
# from .permissions import IsSuperAdmin


# class UserPermissionsView(APIView):
#     serializer_class = UserWithPermissionsSerializer

#     def post(self, request, pk=None, *args, **kwargs):
#         """
#         Add permissions to a specific user (identified by pk).
#         """
#         if not request.user.is_authenticated:
#             return Response({"error": "User is not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)

#         serializer = UserPermissionSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         permission_ids = request.data.get('ids' or [])

#         if pk:
#             try:
#                 user = User.objects.get(pk=pk)

#                 for perm_id in permission_ids:
#                     try:
#                         permission = Permission.objects.get(id=perm_id)
#                         if user.user_permissions.filter(id=perm_id).exists():
#                             # If the user already has this permission, remove it
#                             user.user_permissions.remove(permission)
#                         else:
#                             # If the user does not have this permission, add it
#                             user.user_permissions.add(permission)
#                     except Permission.DoesNotExist:
#                         return Response({"error": f"Permission '{perm_id}' does not exist."}, status=status.HTTP_400_BAD_REQUEST)

#                 user.save()
#                 return Response({"message": "User permissions updated successfully."}, status=status.HTTP_200_OK)

#             except User.DoesNotExist:
#                 return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
#             except Exception as e:
#                 return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({"error": "User ID is required to update permissions."}, status=status.HTTP_400_BAD_REQUEST)


#     def get(self, request, pk=None, *args, **kwargs):
#         """
#         Retrieve all users with permissions or a specific user's permissions.
#         """
#         if pk:
#             try:
#                 user = User.objects.get(pk=pk)
#                 if not user.user_permissions.exists():
#                     return Response({"message": "User has no additional permissions."}, status=status.HTTP_200_OK)
                
#                 serializer = self.serializer_class(user)
#             except User.DoesNotExist:
#                 return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             users_with_permissions = User.objects.filter(user_permissions__isnull=False).distinct()
#             serializer = self.serializer_class(users_with_permissions, many=True)
            
#         return Response(serializer.data, status=status.HTTP_200_OK)


#     def delete(self, request, pk=None, *args, **kwargs):
#         """
#         Remove all permissions from a specific user.
#         """
#         if not request.user.is_authenticated:
#             return Response({"error": "User is not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)

#         if pk:
#             try:
#                 user = User.objects.get(pk=pk)
#                 user.user_permissions.clear()  
#                 return Response({"message": "All additional permissions removed successfully."}, status=status.HTTP_200_OK)
#             except User.DoesNotExist:
#                 return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
#             except Exception as e:
#                 return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({"error": "User ID is required to delete permissions."}, status=status.HTTP_400_BAD_REQUEST)


# # #_____________________________________Personal_________________________________
# # from django.contrib.auth.models import User, Permission
# # # Get the user
# # user = User.objects.get(username='username')

# # # Get the permission
# # permission = Permission.objects.get(codename='add_book')
# # # Assign the permission
# # user.user_permissions.add(permission)

# # # Alternatively, you can grant multiple permissions at once
# # permissions = Permission.objects.filter(codename__in=['add_book', 'change_book'])
# # user.user_permissions.add(*permissions)

# # #________________________________________________________________________________
    













































# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from .models import *
# # from .serializers import *
# # from django.utils import timezone
# # from datetime import date
# # from rest_framework import generics

# # class MarkAttendanceView(APIView):
    
# #     def post(self, request):
# #         serializer = MarkAttendanceSerializer(data=request.data)
# #         if not serializer.is_valid():
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# #         student_class = serializer.validated_data['class_name']
# #         section = serializer.validated_data['section']
# #         status_choice = serializer.validated_data['status']

# #         students = Student.objects.filter(class_name=student_class, section=section)

# #         if not students.exists():
# #             return Response({"error": "No students found for the given class and section."}, status=status.HTTP_404_NOT_FOUND)

# #         updated_count = Attendance.objects.filter(student__in=students).update(status=status_choice)
# #         return Response({"message": f"Attendance updated for {updated_count} student(s)."}, status=status.HTTP_200_OK)











# # # class MarkAttendanceView(APIView):
    
# # #     def post(self, request):
# # #         serializer = MarkAttendanceSerializer(data=request.data)
# # #         if not serializer.is_valid():
# # #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# # #         student_class = serializer.validated_data['class_name']
# # #         section = serializer.validated_data['section']
# # #         status_choice = serializer.validated_data['status']

# # #         students = Student.objects.filter(class_name=student_class, section=section)

# # #         if not students.exists():
# # #             return Response({"error": "No students found for the given class and section."}, status=status.HTTP_404_NOT_FOUND)

# # #         for student in students:
# # #             attendance, created = Attendance.objects.update_or_create(
# # #                 student=student,
# # #                 defaults={'status': status_choice}
# # #             )

# # #         return Response({
# # #             "message": f"Attendance marked sucessfully."
# # #         }, status=status.HTTP_200_OK)


# # # class MarkBulkAttendanceView(APIView):
# # #     def post(self, request, *args, **kwargs):
# # #         serializer = MarkBulkAttendanceSerializer(data=request.data)
        
# # #         if not serializer.is_valid():
# # #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# # #         class_name = serializer.validated_data['class_name']
# # #         section = serializer.validated_data['section']
# # #         student_ids = serializer.validated_data['student_ids']
# # #         status_choice = serializer.validated_data['status']

# # #         students = Student.objects.filter(class_name=class_name, section=section)

# # #         if not students.exists():
# # #             return Response({"message": "No students found for the specified class and section."}, status=status.HTTP_404_NOT_FOUND)


# # #         for student_id in student_ids:
# # #             try:
# # #                 student = students.get(id=student_id)
# # #                 Attendance.objects.update_or_create(
# # #                     student=student,
# # #                     defaults={'status': status_choice}
# # #                 )
                  
# # #             except Student.DoesNotExist:
# # #                 return Response({"error": f"Student with ID {student_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)

# # #         return Response({"message": f"Attendance marked successfully"}, status=status.HTTP_200_OK)




# # # from rest_framework.views import APIView
# # # from rest_framework.response import Response
# # # from rest_framework import status
# # # from .models import Student, Attendance
# # # from django.utils import timezone

# # # class MarkBulkAttendanceView(APIView):
# # #     def post(self, request):
# # #         student_ids = request.data.get('student_ids', [])
# # #         status_value = request.data.get('status') 
# # #         today = timezone.now().date()

# # #         if status_value not in ['Present', 'Absent']:
# # #             return Response({'error': 'Invalid status value.'}, status=status.HTTP_400_BAD_REQUEST)

# # #         for student_id in student_ids:
# # #             try:
# # #                 student = Student.objects.get(id=student_id)

# # #                 attendance, created = Attendance.objects.update_or_create(
# # #                     student=student,
# # #                     date=today,
# # #                     defaults={'status': status_value}
# # #                 )

# # #                 # if not created:
# # #                 #     return Response({'error': f'Attendance for student {student.name} has already been marked for today.'}, status=status.HTTP_400_BAD_REQUEST)

# # #             except Student.DoesNotExist:
# # #                 return Response({'error': f'Student with id {student_id} does not exist.'}, status=status.HTTP_404_NOT_FOUND)

# # #         return Response({'message': 'Attendance marked successfully.'}, status=status.HTTP_200_OK)
    


    
# # # from rest_framework.views import APIView
# # # from rest_framework.response import Response
# # # from rest_framework import status
# # # from .models import Student, Attendance
# # # from datetime import datetime

# # # class MarkAttendanceView(APIView):
# # #     def post(self, request):
# # #         data = request.data
# # #         date_str = data.get('date')

# # #         try:
# # #             attendance_date = datetime.strptime(date_str, '%Y-%m-%d').date()
# # #         except (ValueError, TypeError):
# # #             return Response({"error": "Invalid date format. Use 'YYYY-MM-DD'."}, status=status.HTTP_400_BAD_REQUEST)

# # #         current_date = datetime.now().date()
# # #         if attendance_date != current_date:
# # #             return Response({"error": "Attendance can only be updated for the current date."}, status=status.HTTP_400_BAD_REQUEST)

# # #         attendance_data = data.get('attendance', [])  

# # #         for entry in attendance_data:
# # #             student_id = entry.get('id')
# # #             status_value = entry.get('status')
# # #             try:
# # #                 student = Student.objects.get(student_id=student_id)
# # #                 attendance, created = Attendance.objects.update_or_create(
# # #                     student=student,
# # #                     date=attendance_date,
# # #                     defaults={'status': status_value}
# # #                 )
# # #             except Student.DoesNotExist:
# # #                 continue 

# # #         return Response({"message": "Attendance marked successfully"}, status=status.HTTP_200_OK)


















# # # class MarkAttendanceView(APIView):
    
# # #     def post(self, request):
# # #         student_ids = request.data.get('student_ids', [])
# # #         status_value = request.data.get('status', 'Absent')  
        
# # #         valid_statuses = ['Present', 'Absent']
# # #         if status_value not in valid_statuses:
# # #             return Response({"error": "Invalid attendance status."}, status=status.HTTP_400_BAD_REQUEST)

# # #         students = Student.objects.filter(id__in=student_ids)
        
# # #         if students.exists():
# # #             first_student = students.first()
# # #             same_class_section = students.filter(class_name=first_student.class_name, section=first_student.section)

# # #             for student in same_class_section:
# # #                 Attendance.objects.update_or_create(
# # #                     student=student,
# # #                     date=models.DateField.today(),  
# # #                     defaults={'status': status_value}
# # #                 )
# # #             return Response({"message": "Attendance marked successfully."}, status=status.HTTP_200_OK)
# # #         else:
# # #             return Response({"error": "No students found."}, status=status.HTTP_404_NOT_FOUND)
# # # 



from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status
from django.db import transaction
from django.db.models import Q


class ExamDateSheetAPIView(APIView):

    def get(self, request):
        student_class = request.data.get('class_name', None)
        if student_class:
            exams = Exam.objects.filter(student_class=student_class)
        else:
            exams = Exam.objects.all()
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data)

    def post(self, request):
        if isinstance(request.data, list):
            serializer = ExamSerializer(data=request.data, many=True)
        else:
            serializer = ExamSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({
            "error": "Validation failed for some or all records",
            "details": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        with transaction.atomic():
            for datesheet_data in request.data:
                try:
                    datesheet = Exam.objects.get(id=datesheet_data['id'])
                    serializer = ExamSerializer(datesheet, data=datesheet_data)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                except Exam.DoesNotExist:
                    return Response({"error": f"DateSheet with id {datesheet_data['id']} not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": "DateSheets updated successfully"}, status=status.HTTP_200_OK)


class ResultAPIView(APIView):
    def get(self, request, *args, **kwargs):
        student_id = request.data.get('student_id')
        exam_type_id = request.data.get('exam_type')

        results = Result.objects.all()
        if student_id:
            results = results.filter(student_id=student_id)
        if exam_type_id:
            results = results.filter(exam__examtype_id=exam_type_id)

        serializer = ResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ResultSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        if not isinstance(request.data, list):
            return Response({"error": "Expected a list of results for bulk update."}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            failed_updates = []
            for result_data in request.data:
                if 'id' not in result_data:
                    failed_updates.append({"error": "Missing id for record", "data": result_data})
                    continue

                try:
                    result = Result.objects.get(id=result_data['id'])
                    serializer = ResultSerializer(result, data=result_data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        failed_updates.append({"error": serializer.errors, "data": result_data})
                except Result.DoesNotExist:
                    failed_updates.append({"error": f"Result with id {result_data['id']} not found", "data": result_data})

            if failed_updates:
                return Response({
                    "error": "Some records failed to update.",
                    "failed_updates": failed_updates
                }, status=status.HTTP_400_BAD_REQUEST)
                
        return Response({"message": "Results updated successfully"}, status=status.HTTP_200_OK)
    


from django.apps import apps
from django.db.models import Q  

class SearchView(APIView):
    def get(self, request, *args, **kwargs):
        model_name = request.query_params.get('model', None)  
        search_query = request.query_params.get('search', None) 

        if not model_name:
            return Response({"error": "Model name must be provided."}, status=status.HTTP_400_BAD_REQUEST)  

        try:
            model_class = apps.get_model('message', model_name.capitalize())
            queryset = model_class.objects.all() 
        except LookupError:
            return Response({"error": "Model not found."}, status=status.HTTP_404_NOT_FOUND) 

        if search_query:
            query = Q()
            for field in model_class._meta.get_fields():
                if isinstance(field, (models.CharField, models.TextField)):
                    query |= Q(**{f"{field.name}__icontains": search_query})
            
            # Apply the query to filter results
            queryset = queryset.filter(query)

            if not queryset.exists():
                return Response({"error": f"No matching results for '{search_query}'."}, status=status.HTTP_404_NOT_FOUND)

        serializer_mapping = {
            'result': ResultSerializer,
            'student': StudentSerializer,
            'exam': ExamSerializer,
        }

        serializer_class = serializer_mapping.get(model_name.lower())  

        if not serializer_class:
            return Response({"error": "Unsupported model."}, status=status.HTTP_400_BAD_REQUEST)  
        serialized_data = serializer_class(queryset, many=True).data  

        return Response(serialized_data)

#####################################################################################################################
from rest_framework.generics import GenericAPIView

class EventListAPIView(GenericAPIView):
    serializer_class = EventSerializer

    def get(self, request):
        events = Event.objects.all().order_by('-date')
        serializer = self.serializer_class(events, many=True)
        return Response({"message": "Event List retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)
    
class EventByMonthAPIView(GenericAPIView):
    serializer_class = EventSerializer
    def get(self, request):
        # Get month and year from query parameters
        month = request.query_params.get('month')
        year = request.query_params.get('year')

        if not month or not year:
            return Response({"message": "Month and Year are required parameters"}, status=status.HTTP_400_BAD_REQUEST)

        # Convert month and year to integers and validate
        try:
            month = int(month)
            year = int(year)
            if not (1 <= month <= 12):
                return Response({"message": "Invalid month. It should be between 1 and 12."}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({"message": "Invalid month or year format"}, status=status.HTTP_400_BAD_REQUEST)

        # Filter events based on the month and year
        events = Event.objects.filter(date_year=year, date_month=month).order_by('date')
        if not events.exists():
            return Response({"message": "No events found for the given month and year."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(events, many=True)
        return Response({"message": "Events for the month retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)



























