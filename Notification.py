from plyer import notification
import time

while True:
    notification.notify(
    title = "Notification",
    message = "Drink water",
    timeout = 10
    )
    time.sleep(1)