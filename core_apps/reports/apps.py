from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

import core_apps
import core_apps.reports
import core_apps.reports.signals


class ReportsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.reports"
    verbose_name = _("Reports")

    def ready(self) -> None:
        return core_apps.reports.signals
