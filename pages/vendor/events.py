from nicegui import ui 
from components.sidebar import show_sidebar


@ui.page("/vendor/events")
def show_vendor_events():
     with ui.row().classes("w-full"):
        with ui.column().classes("w-[20%]"):
            show_sidebar()
        with ui.column().classes("w-[80%]"):
            ui.label("Vendor events content goes here")