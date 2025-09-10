from nicegui import ui

def show_header():
    with ui.row().classes(
        "fixed top-0 left-0 w-full justify-between items-center px-8 py-4 bg-black text-white shadow-md z-50"
    ):
        # Logo / App name
        ui.image("Assets/Black & White Minimalist Business Logo.jpeg").classes("w-[100px] h-[70]")

        # Navigation links (spread across)
        with ui.row().classes("flex-1 justify-evenly"):
            ui.link("Home", "/").classes("no-underline text-white hover:text-gray-300")
            ui.link("View Advert", "/view_event").classes("no-underline text-white hover:text-gray-300")
            ui.link("Create Advert", "/add_event").classes("no-underline text-white hover:text-gray-300")
            ui.link("Edit Advert", "/edit_event").classes("no-underline text-white hover:text-gray-300")
            
