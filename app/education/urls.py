from django.urls import path, include

from education import views

urlpatterns = [
    path('schools/', views.school_list, name='school-list'),
    path('<int:school_id>/detail/', views.school_detail, name='detail')
]
