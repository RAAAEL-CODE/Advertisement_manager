from nicegui import ui
import requests
from utils.api import base_url
from functools import partial


def show_home_page():
    response= requests.get(f"{base_url}/adverts")
    json_data = response.json()
     
    with ui.grid().classes(
        "grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 w-full p-6 gap-8 bg-[#e3d5ca]"
    ):
        def product_card(id, image, title, price):
            with ui.column().classes("items-center bg-white rounded-xl shadow-lg p-4 hover:shadow-2xl transition"):
                ui.image(image).classes("w-full max-w-sm h-60 object-cover rounded-lg transition-transform duration-300 hover:scale-105")
                ui.label(title).classes("mt-4 text-2xl font-semibold text-center")
                ui.label(price).classes("text-gray-700 text-lg shadow-sm")
                                
                with ui.row().classes("gap-3 mt-4 flex-wrap justify-center"):
                    ui.button('View', on_click=partial(ui.navigate.to, f"/view_event?id={id}")).classes("bg-black text-white px-4 py-2 rounded-lg")
                    # ui.button('Edit', on_click=lambda: ui.navigate.to(url_edit)).classes("bg-black text-white px-4 py-2 rounded-lg")
                    # ui.button('Delete').classes("bg-black text-white px-4 py-2 rounded-lg")

        # Products
        for product in json_data["data"]:
            product_card(product["id"], product["flyer"], product["title"], f"Price: GHC {product["price"]}")


        

        

                                  