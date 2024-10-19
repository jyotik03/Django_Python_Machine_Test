from django.contrib import admin
from .models import Client, Project

# Admin for Client
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'created_by', 'created_at')  # Display fields in the list view
    search_fields = ('client_name',)
    readonly_fields = ('created_at', 'id')  # Make these fields read-only
    exclude = ('created_by',)  # Automatically set created_by, so exclude it from the form

    # Override save_model to set created_by to the current user
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the client is being created
            obj.created_by = request.user  # Set the creator to the current user
        super().save_model(request, obj, form, change)

# Admin for Project
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'client', 'created_by', 'created_at')
    filter_horizontal = ('users',)  # Allows selection of users via a multi-select widget
    readonly_fields = ('created_at', 'id')
    exclude = ('created_by',)

    # Override save_model to set created_by to the current user
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the project is being created
            obj.created_by = request.user  # Set the creator to the current user
        super().save_model(request, obj, form, change)

admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
