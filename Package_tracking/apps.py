from django.apps import AppConfig

class PackageTrackingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Package_tracking'

    def ready(self):
        import Package_tracking.signals



    
