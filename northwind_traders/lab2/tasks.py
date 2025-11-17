from celery import shared_task
from django.db.models import Sum
from .models import OrderDetail

@shared_task
def generate_monthly_sales_report():
    # simulating heavy CPU calculation
    import time
    time.sleep(10)

    data = (
        OrderDetail.objects
        .values('order__order_date__month')
        .annotate(total=Sum('unit_price'))
        .order_by('order__order_date__month')
    )
    return list(data)


@shared_task
def send_invoices_to_all_customers():
    # simulate slow email sending
    import time
    time.sleep(5)

    for customer in Customer.objects.all():
        # simulate sending email
        print(f"Sending invoice email to {customer.contact_name}")
        time.sleep(0.1)

    return "Invoices sent"