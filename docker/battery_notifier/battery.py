import psutil
import platform

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if percent <= 30 and not plugged:
    if platform.system() == "Windows":
        from pynotifier import Notification

        Notification(
            title="Battery Low",
            description=f"{percent}% Battery remain!!",
            duration=5,
        ).send()
    else:
        print(f"Battery low: {percent}% remaining")

