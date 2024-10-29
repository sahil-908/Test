# from django.db import models
# from django.utils import timezone

# class Student(models.Model):
#     id = models.CharField(max_length=255, primary_key=True)
#     name = models.CharField(max_length=255)
#     rollno = models.CharField(max_length=255)
#     class_name = models.CharField(max_length=255)
#     section = models.CharField(max_length=255)

# class Attendance(models.Model):
#     student = models.ForeignKey("Student", on_delete=models.CASCADE)
#     status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')], default='Absent')
#     date = models.DateField(default=timezone.now)

#     def __str__(self):
#         return f"{self.student} - {self.status} on {self.date}"
    

    
# # class ClassAttendance(models.Model):
# #     student = models.ForeignKey("Student", on_delete=models.CASCADE, related_name='class_attendance')
# #     section = models.ForeignKey("Student", on_delete=models.CASCADE, related_name='section')
# #     status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Absent')
# #     date = models.DateField()




# from django.db import models

# # School Model
# class School(models.Model):
#     name = models.CharField(max_length=50)  
#     school_code = models.CharField(max_length=10)  

#     def __str__(self):
#         return f"{self.name} - {self.school_code}"
    
# # Class Model
# class Class(models.Model):
#     name = models.CharField(max_length=50) 
#     section = models.CharField(max_length=10) 

#     school = models.ForeignKey(School, related_name='school', on_delete=models.CASCADE, blank=True, null=True)

#     def __str__(self):
#         return f"{self.name} - {self.section}"

# # Timetable Model
# class Timetable(models.Model):
#     DAY_CHOICES = [
#         ('Monday', 'Monday'),
#         ('Tuesday', 'Tuesday'),
#         ('Wednesday', 'Wednesday'),
#         ('Thursday', 'Thursday'),
#         ('Friday', 'Friday')
#     ]

#     day = models.CharField(max_length=10, choices=DAY_CHOICES)
#     start_time = models.CharField(max_length=20)
#     end_time = models.CharField(max_length=20)
#     subject = models.CharField(max_length=100)
    
#     school_class = models.ForeignKey(Class, related_name='timetables', on_delete=models.CASCADE)


# # Syllabus Model

# class Subject(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

# class Syllabus(models.Model):
#     subject = models.ForeignKey(Subject, related_name='syllabus', on_delete=models.CASCADE)
#     file = models.FileField(upload_to='syllabus_files/') 
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.subject.name} - {self.file.name}"
    



# class Hobbies(models.Model):
#     hobbies = models.JSONField()  
#     relationship_status = models.JSONField()
#     drink = models.JSONField()
#     language = models.JSONField()
#     Address = models.CharField(max_length=255, blank=True, null=True)
#     job_title = models.CharField(max_length=255, blank=True, null=True)


from django.db import models
import uuid

class Exam(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_class = models.CharField(max_length=10, blank=True)  
    subject = models.CharField(max_length=100, blank=True)
    date = models.DateField()
    time = models.TimeField()
    examtype = models.ForeignKey("ExamType", on_delete=models.CASCADE) 
    mode = models.CharField(max_length=100, blank=True)
    center = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.subject} - {self.student_class}"
     
class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=True)
    student_class = models.CharField(max_length=10, blank=True)  
    roll_number = models.CharField(max_length=10, unique=True, blank=True)  

    def __str__(self):
        return f"{self.name} - {self.student_class}"

class ExamType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=True) 


    def __str__(self):
        return self.name

class Result(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE) 
    marks_obtained = models.FloatField()
    total_marks = models.FloatField()
    grade = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return f"{self.student} - {self.exam.subject} ({self.exam.examtype})"
    
class Event(models.Model):
    date = models.DateField()
    event = models.CharField(max_length=255)
    status = models.CharField(max_length=50)

    def _str_(self):
        return self.event
    



































