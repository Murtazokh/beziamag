from django.contrib import admin
from .models import About, Testimonial, Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    search_fields = ('name', 'email', 'subject')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'role', 'visible')
    list_filter = ('visible',)
    list_editable = ('visible',)