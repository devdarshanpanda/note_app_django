from django.urls import path
from appone import views
urlpatterns = [
    path('',views.home,name='home'),
    # path('add_note/',views.add_note,name='add_note'),
    path('add_note/',views.add_note,name='add_note'),
    path('save_note/',views.save_note,name='save_note'),
    path('signup/',views.signup.as_view(),name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('mynotes/',views.my_notes,name='my_notes'),
    path('edit_notes/<int:id>',views.edit_notes,name='edit_notes'),
    path('delete_notes/<int:id>',views.delete_notes,name='delete_notes'),
]
