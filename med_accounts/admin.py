from django.contrib import admin
from models import MyDoctor
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import MyDoctor, Patients
from .forms import UserChangeForm, UserCreationForm
# Register your models here.


class MyDoctorAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name', 'email', 'is_admin', 'is_member', 'country', 'specialite')
    list_filter = ('is_admin', 'is_member')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('owner_first_name', 'owner_last_name', 'country', 'specialite')}),
        ('Permissions', {'fields': ('is_admin', 'is_member')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password1', 'password2', 'owner_first_name', 'owner_last_name', 'country', 'specialite',)
        }),
    )
    search_fields = ('email', 'name', 'owner_first_name', 'owner_last_name', 'country', 'specialite')
    ordering = ('name',)
    filter_horizontal = ()

#Register the new UserAdmin
admin.site.register(Patients)
admin.site.register(MyDoctor, MyDoctorAdmin)
#unregister the group model admin

