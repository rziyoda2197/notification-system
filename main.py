import threading
import time
import queue

class NotificationSystem:
    def __init__(self):
        self.queue = queue.Queue()

    def send_notification(self, message):
        self.queue.put(message)

    def receive_notification(self):
        while True:
            message = self.queue.get()
            print(f"Notification: {message}")
            self.queue.task_done()

    def start(self):
        thread = threading.Thread(target=self.receive_notification)
        thread.daemon = True
        thread.start()

    def stop(self):
        self.queue.join()

# Misol
notification_system = NotificationSystem()
notification_system.start()

while True:
    notification_system.send_notification("Hello, world!")
    time.sleep(1)
    notification_system.send_notification("This is a notification system.")
    time.sleep(1)
    notification_system.stop()
    break
```

Kodda quyidagilar mavjud:

*   `NotificationSystem` klassi notification systemni yaratish uchun ishlatiladi.
*   `send_notification` metodi notificationni qo'shish uchun ishlatiladi.
*   `receive_notification` metodi notificationni qabul qilish uchun ishlatiladi.
*   `start` metodi notification systemni boshlash uchun ishlatiladi.
*   `stop` metodi notification systemni to'xtatish uchun ishlatiladi.
*   Misolda notification systemni yaratib, boshlash va to'xtatish uchun ishlatiladi.
