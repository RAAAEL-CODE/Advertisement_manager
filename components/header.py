from nicegui import ui

def show_header():
    with ui.row().classes(
        "w-full bg-gray-900 text-white px-8 py-4 shadow-md justify-between items-center fixed"
    ):
        # Logo / App name
        ui.image("Assets/Black & White Minimalist Business Logo.jpeg").classes("w-[100px] h-[70]")

        # Navigation links (spread across)
        with ui.row().classes("flex-1 justify-evenly"):
            ui.link("Home", "/").classes("no-underline text-white hover:text-gray-300")
            ui.link("Add Event", "/add_event").classes("no-underline text-white hover:text-gray-300")
            ui.link("Edit Event", "/edit_event").classes("no-underline text-white hover:text-gray-300")
            ui.link("View Events", "/view_event").classes("no-underline text-white hover:text-gray-300")
