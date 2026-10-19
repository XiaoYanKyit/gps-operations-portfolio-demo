from django.contrib import admin
from .models import GPSResetLog, OutletRemovalLog


admin.site.site_header = "GPS Operations Demo • System Administration"
admin.site.site_title = "GPS Operations Demo Admin"
admin.site.index_title = "System Administration"


@admin.register(GPSResetLog)
class GPSResetLogAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "user",
        "card_code",
        "ship_to_code",
        "reset_type",
        "status",
        "message",
    )
    list_filter = ("status", "reset_type", "created_at")
    search_fields = (
        "card_code",
        "ship_to_code",
        "user__username",
        "user__first_name",
        "user__last_name",
        "message",
    )
    ordering = ("-created_at",)
    list_per_page = 25
    readonly_fields = ("created_at",)


@admin.register(OutletRemovalLog)
class OutletRemovalLogAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "user",
        "code",
        "customer_code",
        "removal_type",
        "status",
        "message",
    )
    list_filter = ("status", "removal_type", "created_at")
    search_fields = (
        "code",
        "customer_code",
        "user__username",
        "user__first_name",
        "user__last_name",
        "message",
    )
    ordering = ("-created_at",)
    list_per_page = 25
    readonly_fields = ("created_at",)
