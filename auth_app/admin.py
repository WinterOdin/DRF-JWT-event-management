from django.contrib.auth.admin import UserAdmin
from auth_app.models import CustomUser, Company
from django.forms import Textarea
from django.contrib import admin
from django.db import models


class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ("email", "user_name", "first_name", "company")
    list_filter = (
        "email",
        "user_name",
        "first_name",
        "is_active",
        "is_staff",
        "company",
    )
    ordering = ("-created",)
    list_display = ("email", "user_name", "first_name", "is_active", "is_staff")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "user_name",
                    "first_name",
                    "company",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )

    formfield_overrides = {
        models.TextField: {"widget": Textarea(attrs={"rows": 20, "cols": 60})},
    }

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "user_name",
                    "first_name",
                    "password1",
                    "password2",
                    "company",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


admin.site.register(CustomUser, UserAdminConfig)
admin.site.register(Company)
