from nicegui import ui 

def show_view_page():
    
    with ui.card().classes("w-full h-full sm:w-[90%] md:w-[70%] lg:w-[60%] mx-auto p-6 bg-white rounde-xl shadow-lg"):
        ui.image("Assets/the-last-shirt-1510597_1280.jpg").classes("w-full h-48 sm:h-60 rounded-lg mb-4 shadow-xl transition-transform duration-300 hover:scale-110")
        ui.label("Euro Shirt").classes("text-xl font-semibold")
        ui.label("price:ghc 150").classes("text-gray-700 text-xl shadow-xl")
        ui.label("category: Fashion")
        ui.label("Description: A single mordern sofa with plush cushions-Elastic silky fiber fabric. Available in different colors. visit shop for a 50% discount ").classes("text-grey-600 mb-2")
            