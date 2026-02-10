# products/tasks.py
from celery import shared_task # type: ignore
from time import sleep

@shared_task
def send_product_notification(product_id):
    sleep(5)
    print(f"Notification sent for product {product_id}")
