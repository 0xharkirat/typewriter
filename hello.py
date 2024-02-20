import flet as ft
import time
import pyautogui
import threading

def main(page: ft.Page):
    # Function to log events
    def logger_event(event):
        lv.controls.append(ft.Text(event))
        page.update()

    # Function to clear text area.
    def clear_text_area(e):
        textarea.value = ""
        page.update()

    # Function to update Start button state based on text change
    def update_start_button_state():
        if textarea.value.strip():  # Check if the text area is not empty
            startButton.disabled = False

        else:
            startButton.disabled = True
        
        page.update()

    # Function to detect text area change.
    def textarea_change(e):
        update_start_button_state()


    # Function to start typing
    def start_typing(e):
        try:
            pyautogui.FAILSAFE = True
            textarea.read_only = True
            startButton.disabled = True
            clearText.disabled = True
            lv.controls.clear()
            page.update()
            logger_event("Typing will start in 5 seconds...")
            for i in range(5, 0, -1):
                logger_event(f"Starting in {i} seconds...")
                time.sleep(1)
                page.update()
            
            text = textarea.value  # Opening the text file
            logger_event("Typing started")
            
            pyautogui.typewrite(text)
            
            logger_event("Typing finished")

            textarea.read_only = False
            startButton.disabled = False
            clearText.disabled = False
            page.update()

        except pyautogui.FailSafeException:
            # Re-enable the start button and the text area if fail-safe is triggered
            textarea.read_only = False
            startButton.disabled = False
            clearText.disabled = False
            logger_event("Failsafe triggered.")
            logger_event("Start again.")
            
            page.update()

    # UI
    page.title = "Automate Typewriter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
   

    textarea = ft.TextField(label="Paste text here.", multiline=True, min_lines=1, max_lines=20, on_change=textarea_change)
    startButton = ft.ElevatedButton(text="Start Typing", disabled=True, on_click=start_typing, tooltip="Paste some text above first.")
    clearText = ft.ElevatedButton(text="Clear", on_click=clear_text_area, bgcolor=ft.colors.RED_300,
                                color=ft.colors.WHITE,)
    failSafeText = ft.Text("\"Move the mouse cursor to the top-left corner of screen to stop execution.\"")
    buttonRows = ft.Row(expand=0, controls=[startButton, clearText, failSafeText])


    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    page.add(textarea, buttonRows, lv)

    

ft.app(target=main)
