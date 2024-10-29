# from django.urls import path
# from .views import *

# urlpatterns = [
#     # path('timetable/', BulkTimetableView.as_view(), name='timetable'),
#     # path('subject/upload/', SubjectBulkUploadView.as_view(), name='subject-bulk-upload'),

#     # path('hobbies/', HobbiesAPIView.as_view(), name='userprofile-list-create'),
#     # path('hobbies/<int:pk>/', HobbiesAPIView.as_view(), name='userprofile-detail'),

#     path('permissions/<int:user_id>/', UserPermissionsView.as_view(), name='change_user_permissions'),
#     path('permissions/', UserPermissionsView.as_view(), name='list-users-permissions'),

# ]



from django.urls import path
from .views import *

urlpatterns = [
    # path(' /', ExamDateSheetAPIView.as_view(), name='exam_datesheet'),
    # path('result/', ResultAPIView.as_view(), name='results'),
    
    # path('search/', SearchView.as_view(), name='multi_model_search'),

    path('events/', EventListAPIView.as_view(), name='event-list-api'),
    path('events/by-month/', EventByMonthAPIView.as_view(), name='event-by-month-api'),
]



