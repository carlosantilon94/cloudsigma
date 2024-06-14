from celery import shared_task
import time

@shared_task(bind=True)
def test_func(self):
    progress = 0
    for i in range(10):
        time.sleep(10)  # Simulate an operation that takes too long
        progress += 10
        self.update_state(state='PROGRESS', meta={'current': progress, 'total': 100})
    return "Done"