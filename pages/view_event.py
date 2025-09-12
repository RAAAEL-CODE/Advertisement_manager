from nicegui import ui
import requests
from utils.api import base_url


def show_view_page(id):
    response = requests.get(f"{base_url}/adverts/{id}")
    json_data = response.json()
    advert = json_data["data"]

    def delete_advert():
        response = requests.delete(f"{base_url}/adverts/{id}")
        if response.status_code == 200:
            ui.navigate.to("/")

    with ui.card().classes("w-full h-full sm:w-[90%] md:w-[70%] lg:w-[60%] mx-auto p-6 bg-white rounde-xl shadow-lg mt-24"):
        ui.image(advert["flyer"]).classes("w-full h-full rounded-lg mb-4 shadow-xl transition-transform duration-300 hover:scale-110")
        ui.label(advert["title"]).classes("text-xl font-semibold")
        ui.label(f"price:ghc {advert["price"]}").classes("text-gray-700 text-xl shadow-xl")
        ui.label(f"Category: {advert["category"]}").classes("text-xl")
        ui.label(f'Description: {advert["description"]}').classes("text-grey-600 text-xl")
        ui.button("Buy Item").classes("w-full self-center bg-black")
        url = 'http://127.0.0.1:8080/'
        with ui.grid(columns=2).classes("items-center justify-center self-center"):    
            ui.button('Exit', on_click=lambda: ui.navigate.to(url)).classes("bg-black w-[200px] text-white px-4 py-2 rounded-lg")
            ui.button('Delete', on_click=delete_advert).classes("bg-black w-[200px] text-white px-4 py-2 rounded-lg ")
        
