from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    # This is where you can add customizations for the list display,
    # list filters, search fields, etc., of the Profile model in the admin page.
    list_display = ('user', 'bio', 'other_fields')
    list_filter = ('user',)
    search_fields = ('user__username', 'user__email', 'bio')
    # If your Profile model has many fields, you might want to consider adding fieldsets
    # or using a custom form to simplify the layout in the admin interface.

    # Assume 'other_fields' represents other fields from the 'Profile' model.
    # You should replace it with the actual field names.

admin.site.register(Profile, ProfileAdmin)