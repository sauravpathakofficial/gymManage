from django.urls import path
from . import views

app_name='gymManage'
urlpatterns = [
    path('', views.home, name="gym-manager"),
    path('membership/',views.membership,name="membership"),
    path('member/',views.member,name="member"),
    path('createGymMembership/',views.createGymMemberShip,name="createGymMembership"),
    path('createGymMember/',views.createGymMember,name="createGymMember"),
    path('updateGymMembership/<int:id>', views.updateGymMembership, name='updateGymMembership'),
    path('updateGymMembership/updaterecord/<int:id>', views.updateGymMembershipRecord, name='updateGymMembershipRecord'),
    path('updateGymMember/<int:id>', views.updateGymMember, name='updateGymMember'),
    path('updateGymMember/updaterecord/<int:id>', views.updateGymMemberRecord, name='updateGymMemberRecord'),
]
