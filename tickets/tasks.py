from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email(**kwargs):
    ticket = kwargs['ticket'].capitalize()
    send_mail(
        f"Status «{ticket}» is changed",
        f"Dear {kwargs['user'].title()}! Your status of ticket «{ticket}»"
        f" is changed from «{kwargs['current_status']}»"
        f" to «{kwargs['new_status']}».",
        'fakekrolchatka@gmail.com',
        (kwargs['email'],),
        fail_silently=False
    )
    return f'Send notification on email {kwargs["email"]}'
