def clear_cache_task():
    from django.core.cache import cache
    cache.clear()
from django.core.mail import send_mail


def send_email_task(to_email, subject, body):
    send_mail(
        subject,
        body,
        "noreply@myapp.com",
        [to_email],
        fail_silently=False,
    )

