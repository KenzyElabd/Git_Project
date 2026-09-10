import importlib
import time

import psutil

try:
    Notification = importlib.import_module("winotify").Notification
except ImportError:  # pragma: no cover - fallback for environments without winotify
    class Notification:
        def __init__(self, app_id, title, msg):
            self.app_id = app_id
            self.title = title
            self.msg = msg

        def show(self):
            print(f"{self.title}: {self.msg}")



notified = False

while True:
    battery = psutil.sensors_battery()

    percent = battery.percent
    plugged = battery.power_plugged

    print(f"Battery: {percent}% | Charger: {plugged}")

    if percent <= 30 and not plugged:

        if not notified:
            notification = Notification(
                app_id="Battery Monitor",
                title="Battery Low",
                msg=f"{percent}% Battery remaining!"
            )

            notification.show()
            notified = True

    else:
        notified = False

    time.sleep(60)