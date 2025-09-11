# from nicegui import ui

       
# def show_home_page():
#     with ui.grid(columns=3).classes("w-screen h-screen justify-center p-8 gap-12 mx-8 items-start"):
#         with ui.column().classes("w-72 items-center"):
#             ui.image("Assets/furniture-5966893_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xl transition-transform duration-300 hover:scale-110")
#             ui.label("Single Sofa").classes("mt-4 text-4xl font-semibold")
#             ui.label("price:ghc 1000").classes("text-gray-700 text-xl shadow-xl")
#             url_view = 'http://127.0.0.1:8080/view_event'
#             url_edit = 'http://127.0.0.1:8080/edit_event'

#             with ui.row().classes("gap-4 mt-4"):  # buttons in a row with spacing
#                 ui.button('View', on_click=lambda: ui.navigate.to(url_view)).classes("bg-black text-white px-4 py-2 rounded-lg")
#                 ui.button('Edit', on_click=lambda: ui.navigate.to(url_edit)).classes("bg-black text-white px-4 py-2 rounded-lg")
#                 ui.button('Delete').classes("bg-black text-white px-4 py-2 rounded-lg")




#         with ui.column().classes("w-72 items-center"):
#             ui.image("Assets/the-last-shirt-1510597_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xl transition-transform duration-300 hover:scale-110")
#             ui.label("Euro Shirt").classes("mt-4 text-4xl font-semibold")
#             ui.label("price:ghc 150").classes("text-gray-700 text-xl shadow-xl")
#             url_view = 'http://127.0.0.1:8080/view_event'
#             url_edit = 'http://127.0.0.1:8080/edit_event'

#             with ui.row().classes("gap-4 mt-4"):  # buttons in a row with spacing
#                 ui.button('View', on_click=lambda: ui.navigate.to(url_view)).classes("bg-black text-white px-4 py-2 rounded-lg")
#                 ui.button('Edit', on_click=lambda: ui.navigate.to(url_edit)).classes("bg-black text-white px-4 py-2 rounded-lg")
#                 ui.button('Delete').classes("bg-black text-white px-4 py-2 rounded-lg")

    
#         with ui.column().classes("w-72 items-center"):
#             ui.image("Assets/fashion-6203956_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xltransition-transform duration-300 hover:scale-110")
#             ui.label("Gown").classes("mt-4 text-4xl font-semibold")
#             ui.label("price:ghc 5000").classes("text-gray-700 text-xl shadow-xl")
#             url_view = 'http://127.0.0.1:8080/view_event'
#             url_edit = 'http://127.0.0.1:8080/edit_event'

#             with ui.row().classes("gap-4 mt-4"):  # buttons in a row with spacing
#                 ui.button('View', on_click=lambda: ui.navigate.to(url_view)).classes("bg-black text-white px-4 py-2 rounded-lg")
#                 ui.button('Edit', on_click=lambda: ui.navigate.to(url_edit)).classes("bg-black text-white px-4 py-2 rounded-lg")
#                 ui.button('Delete').classes("bg-black text-white px-4 py-2 rounded-lg")


#         with ui.column().classes("w-72 items-center"):
#             ui.image("Assets/water-bottle-898332_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xl transition-transform duration-300 hover:scale-110")
#             ui.label("Water-bottle").classes("mt-4 text-4xl font-semibold")
#             ui.label("price:ghc 50").classes("text-gray-700 text-xl shadow-xl")
#             url_view = 'http://127.0.0.1:8080/view_event'
#             url_edit = 'http://127.0.0.1:8080/edit_event'

#             with ui.row().classes("gap-4 mt-4"):  # buttons in a row with spacing
#                 ui.button('View', on_click=lambda: ui.navigate.to(url_view)).classes("bg-black text-white px-4 py-2 rounded-lg")
#                 ui.button('Edit', on_click=lambda: ui.navigate.to(url_edit)).classes("bg-black text-white px-4 py-2 rounded-lg")
#                 ui.button('Delete').classes("bg-black text-white px-4 py-2 rounded-lg")

    
#         with ui.column().classes("w-72 items-center"):
#             ui.image("Assets/travel-bag-4326732_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xl transition-transform duration-300 hover:scale-110")
#             ui.label("Travel Bag").classes("mt-4 text-4xl font-semibold")
#             ui.label("price:ghc 700").classes("text-gray-700 text-xl shadow-xl")
#             url_view = 'http://127.0.0.1:8080/view_event'
#             url_edit = 'http://127.0.0.1:8080/edit_event'

#             with ui.row().classes("gap-4 mt-4"):  # buttons in a row with spacing
#                 ui.button('View', on_click=lambda: ui.navigate.to(url_view)).classes("bg-black text-white px-4 py-2 rounded-lg")
#                 ui.button('Edit', on_click=lambda: ui.navigate.to(url_edit)).classes("bg-black text-white px-4 py-2 rounded-lg")
#                 ui.button('Delete').classes("bg-black text-white px-4 py-2 rounded-lg")

    
#         with ui.column().classes("w-72 items-center"):
#             ui.image("Assets/vehicle-2132360_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xl transition-transform duration-300 hover:scale-110")
#             ui.label("1987 Vintage car").classes("mt-4 text-4xl font-semibold") 
#             ui.label("price:ghc 3000000").classes("text-gray-700 text-xl shadow-xl")
#             url_view = 'http://127.0.0.1:8080/view_event'
#             url_edit = 'http://127.0.0.1:8080/edit_event'

#             with ui.row().classes("gap-4 mt-4"):  # buttons in a row with spacing
#                 ui.button('View', on_click=lambda: ui.navigate.to(url_view)).classes("bg-black text-white px-4 py-2 rounded-lg")
#                 ui.button('Edit', on_click=lambda: ui.navigate.to(url_edit)).classes("bg-black text-white px-4 py-2 rounded-lg")
#                 ui.button('Delete').classes("bg-black text-white px-4 py-2 rounded-lg")

    
#         with ui.column().classes("w-72 items-center"):
#             ui.image("Assets/bag-1052370_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xl transition-transform duration-300 hover:scale-110")
#             ui.label("Ladies bag").classes("mt-4 text-4xl font-semibold")
#             ui.label("price:ghc 400").classes("text-gray-700 text-xl shadow-xl")
#             url_view = 'http://127.0.0.1:8080/view_event'
#             url_edit = 'http://127.0.0.1:8080/edit_event'

#             with ui.row().classes("gap-4 mt-4"):  # buttons in a row with spacing
#                 ui.button('View', on_click=lambda: ui.navigate.to(url_view)).classes("bg-black text-white px-4 py-2 rounded-lg")
#                 ui.button('Edit', on_click=lambda: ui.navigate.to(url_edit)).classes("bg-black text-white px-4 py-2 rounded-lg")
#                 ui.button('Delete').classes("bg-black text-white px-4 py-2 rounded-lg")


#         with ui.column().classes("w-72 items-center"):
#             ui.image("Assets/chairs-2181960_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xl transition-transform duration-300 hover:scale-110")
#             ui.label("Dinning table set").classes("mt-4 text-4xl font-semibold")
#             ui.label("price:ghc 3000").classes("text-gray-700 text-xl shadow-xl")
#             url_view = 'http://127.0.0.1:8080/view_event'
#             url_edit = 'http://127.0.0.1:8080/edit_event'

#             with ui.row().classes("gap-4 mt-4"):  # buttons in a row with spacing
#                 ui.button('View', on_click=lambda: ui.navigate.to(url_view)).classes("bg-black text-white px-4 py-2 rounded-lg")
#                 ui.button('Edit', on_click=lambda: ui.navigate.to(url_edit)).classes("bg-black text-white px-4 py-2 rounded-lg")
#                 ui.button('Delete').classes("bg-black text-white px-4 py-2 rounded-lg")


#         with ui.column().classes("w-72 items-center"):
#             ui.image("Assets/mug-5161566_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xl transition-transform duration-300 hover:scale-110")
#             ui.label("Mug").classes("mt-4 text-4xl font-semibold")
#             ui.label("price:ghc 80").classes("text-gray-700 text-xl shadow-xl")
#             url_view = 'http://127.0.0.1:8080/view_event'
#             url_edit = 'http://127.0.0.1:8080/edit_event'

#             with ui.row().classes("gap-4 mt-4"):  # buttons in a row with spacing
#                 ui.button('View', on_click=lambda: ui.navigate.to(url_view)).classes("bg-black text-white px-4 py-2 rounded-lg")
#                 ui.button('Edit', on_click=lambda: ui.navigate.to(url_edit)).classes("bg-black text-white px-4 py-2 rounded-lg")
#                 ui.button('Delete').classes("bg-black text-white px-4 py-2 rounded-lg")

                                        
from nicegui import ui
import os

def show_home_page():
    with ui.grid().classes(
        "grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 w-full p-6 gap-8 bg-[#e3d5ca]"
    ):
        def product_card(image, title, price):
            with ui.column().classes("items-center bg-white rounded-xl shadow-lg p-4 hover:shadow-2xl transition"):
                ui.image(image).classes("w-full max-w-sm h-60 object-cover rounded-lg transition-transform duration-300 hover:scale-105")
                ui.label(title).classes("mt-4 text-2xl font-semibold text-center")
                ui.label(price).classes("text-gray-700 text-lg shadow-sm")
                
                url_view = 'http://127.0.0.1:8080/view_event'
                url_edit = 'http://127.0.0.1:8080/edit_event'
                
                with ui.row().classes("gap-3 mt-4 flex-wrap justify-center"):
                    ui.button('View', on_click=lambda: ui.navigate.to(url_view)).classes("bg-black text-white px-4 py-2 rounded-lg")
                    ui.button('Edit', on_click=lambda: ui.navigate.to(url_edit)).classes("bg-black text-white px-4 py-2 rounded-lg")
                    ui.button('Delete').classes("bg-black text-white px-4 py-2 rounded-lg")

        # Products
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
        

        

                                  