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
<<<<<<< HEAD
        for product in json_data["data"]:
            product_card(product["id"], product["flyer"], product["title"], f"Price: GHC {product["price"]}")
=======
        product_card("Assets/furniture-5966893_1280.jpg", "Single Sofa", "Price: GHC 1000")
        product_card("Assets/the-last-shirt-1510597_1280.jpg", "Euro Shirt", "Price: GHC 150")
        product_card("Assets/fashion-6203956_1280.jpg", "Gown", "Price: GHC 5000")
        product_card("Assets/water-bottle-898332_1280.jpg", "Water-bottle", "Price: GHC 50")
        product_card("Assets/travel-bag-4326732_1280.jpg", "Travel Bag", "Price: GHC 700")
        product_card("Assets/vehicle-2132360_1280.jpg", "1987 Vintage car", "Price: GHC 3000000")
        product_card("Assets/bag-1052370_1280.jpg", "Ladies Bag", "Price: GHC 400")
        product_card("Assets/chairs-2181960_1280.jpg", "Dining Table Set", "Price: GHC 3000")
        product_card("Assets/mug-5161566_1280.jpg", "Mug", "Price: GHC 80")
        product_card("Assets/bedroom-5772286_1280.jpg","Bed","Price: GHC 5000")
        product_card("Assets/mercedes-3417100_1280.jpg","Mercedes","Price:GHS 6000000")
        

        

>>>>>>> d491f139069116fda0296719f1ef1f5e04aa8cfb
                                  