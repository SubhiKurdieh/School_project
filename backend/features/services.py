from django.utils import timezone
from finance.models import Invoice
from .models import FeatureFlag

ALWAYS_ALLOWED = [
    'emergency_notifications',
    'bus',
    'schedule',
]

def is_feature_allowed(user, feature_name):
    # 1. Admin override (temporary or permanent)
    override = FeatureFlag.objects.filter(
        user=user,
        feature=feature_name,
        enabled=True
    ).filter(
        expires_at__isnull=True
    ).first() or FeatureFlag.objects.filter(
        user=user,
        feature=feature_name,
        enabled=True,
        expires_at__gte=timezone.now()
    ).first()

    if override:
        return True

    # 2. Always allowed features
    if feature_name in ALWAYS_ALLOWED:
        return True

    # 3. Financial blocking
    has_late_invoice = Invoice.objects.filter(
        student__parents=user,
        status='late'
    ).exists()

    return not has_late_invoice