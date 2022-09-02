from django.core.mail import send_mail

from store import settings


def send_checkout_email(subject, msg, recipient_email):
    send_mail(
        subject=subject,
        message=msg,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[recipient_email]
    )
