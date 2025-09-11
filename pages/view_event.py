from nicegui import ui 


def show_view_page():
    with ui.column().classes("bg-[#e3d5ca]"):
        with ui.card().classes("w-full h-full sm:w-[90%] md:w-[70%] lg:w-[60%] mx-auto p-6 bg-white rounde-xl shadow-lg mt-24  "):
            ui.image("Assets/furniture-5966893_1280.jpg").classes("w-full h-full rounded-lg mb-4 shadow-xl transition-transform duration-300 hover:scale-110")
            ui.label("Single Sofa").classes("text-xl font-semibold")
            ui.label("price:ghc 150").classes("text-gray-700 text-xl shadow-xl")
            ui.label("Category: Furniture").classes("text-xl")
            ui.label("Description: A single mordern sofa with plush cushions-Elastic silky fiber fabric. Available in different colors. Gentle on skin and sutable for every place being it office,hall or bedroom. very good for elderlys that needs a good rest time." \
            "visit shop for a 50% discount ").classes("text-grey-600 text-xl")
            ui.button("Buy Item").classes("w-full self-center")
            url = 'http://127.0.0.1:8080/'
            ui.button('Exit', on_click=lambda: ui.navigate.to(url)).classes("self-center")
            