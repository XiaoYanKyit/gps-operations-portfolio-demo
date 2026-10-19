from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),

    path(
        "gps-cancel/",
        views.gps_cancel,
        name="gps_cancel"
    ),

    path(
        "activity/",
        views.activity,
        name="activity"
    ),

    path(
        "remove-outlet/",
        views.remove_outlet,
        name="remove_outlet"
    ),

    path(
        "export/activity-logs/",
        views.export_activity_logs,
        name="export_activity_logs"
        ),
]