# from nicegui import ui
# import requests
# from utils.api import base_url
# from functools import partial


# def show_home_page():
#     response= requests.get(f"{base_url}/adverts")
#     json_data = response.json()
     
#     with ui.grid().classes(
#         "grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 w-full p-6 gap-8 bg-[#e3d5ca]"
#     ):
#         def product_card(id, image, title, price):
#             with ui.column().classes("items-center bg-white rounded-xl shadow-lg p-4 hover:shadow-2xl transition"):
#                 ui.image(image).classes("w-full max-w-sm h-60 object-cover rounded-lg transition-transform duration-300 hover:scale-105")
#                 ui.label(title).classes("mt-4 text-2xl font-semibold text-center")
#                 ui.label(price).classes("text-gray-700 text-lg shadow-sm")
                                
#                 with ui.row().classes("gap-3 mt-4 flex-wrap justify-center"):
#                     ui.button('View', on_click=partial(ui.navigate.to, f"/view_event?id={id}")).classes("bg-black text-white px-4 py-2 rounded-lg")
            


#                     # Create a button that opens the dialog on click
                
#                     # ui.button('Edit', on_click=lambda: ui.navigate.to(url_edit)).classes("bg-black text-white px-4 py-2 rounded-lg")
#                     # ui.button('Delete').classes("bg-black text-white px-4 py-2 rounded-lg")

#         # Products
#         for product in json_data["data"]:
#             product_card(product["id"], product["flyer"], product["title"], f"Price: GHC {product["price"]}")
from nicegui import ui, app
import requests
from utils.api import base_url
from functools import partial

# We'll use a global variable to store the events data once fetched
events_data = []

@ui.page('/home')
def show_home_page():
    global events_data

    # Fetch data every time the page is loaded
    try:
        response = requests.get(f"{base_url}/adverts")
        response.raise_for_status()  # Raise an exception for bad status codes
        events_data = response.json()["data"] # Update the global variable with fresh data
    except requests.exceptions.RequestException as e:
        ui.notify(f"Failed to fetch events: {e}", type="negative")
        events_data = []

    # UI layout for the home page
    with ui.row().classes("w-full items-center"):
        # Placeholder for the video (replace with your actual video component)
        ui.label("All Items").classes("text-3xl font-bold ml-20")

        # Search bar and button using NiceGUI components
        with ui.row().classes("w-[600px] justify-center items-center gap-4 py-4 ml-[500px]"):
            search_input = ui.input(placeholder="Search items...").classes("w-2/3 md:w-1/2").props('outlined dense')
            ui.button(icon="search", on_click=lambda: display_events(search_input.value)).classes("bg-black text-white px-4 py-2 rounded-lg")

        # A refreshable grid to display events based on search
        @ui.refreshable
        def display_events(search_term=""):
            events_grid.clear()  # Clear the existing grid content

            search_term = search_term.lower().strip()
            
            # Filter events based on the search term
            if search_term:
                filtered_events = [
                    event for event in events_data
                    if any(search_term in str(value).lower() for value in event.values())
                ]
            else:
                filtered_events = events_data

            if not filtered_events:
                with events_grid:
                    ui.label("No events found.").classes("text-lg text-gray-500 text-center w-full")
            else:
                with events_grid:
                    for event in filtered_events:
                        product_card(event["id"], event["flyer"], event["title"], f"Price: GHC {event["price"]}")

    # The grid container for the event cards
    events_grid = ui.grid().classes(
        "grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 w-full p-6 gap-8 bg-[#e3d5ca]"
    )

    # Function to create an individual product card
    def product_card(id, image, title, price):
        with ui.column().classes("items-center bg-white rounded-xl shadow-lg p-4 hover:shadow-2xl transition"):
            ui.image(image).classes("w-full max-w-sm h-60 object-cover rounded-lg transition-transform duration-300 hover:scale-105")
            ui.label(title).classes("mt-4 text-2xl font-semibold text-center")
            ui.label(price).classes("text-gray-700 text-lg shadow-sm")
            with ui.row().classes("gap-3 mt-4 flex-wrap justify-center"):
                ui.button('View', on_click=partial(ui.navigate.to, f"view_event/{id}")).classes("bg-black text-white px-4 py-2 rounded-lg")

    # Initial display of all events
    display_events()