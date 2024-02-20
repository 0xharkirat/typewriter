import flet as ft
from time import sleep
import threading

def main(page: ft.Page):
    page.title = "Event Logger"
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    page.add(lv)

    def logger_event(event):
        lv.controls.append(ft.Text(event))
        page.update()

    # Function to simulate events and log them
    def simulate_events():
        count = 1
        for i in range(0, 60):
            event = f"Event {count}"
            logger_event(event)
            count += 1
            sleep(1)

    # Start a separate thread to simulate events
    threading.Thread(target=simulate_events).start()

ft.app(target=main)
