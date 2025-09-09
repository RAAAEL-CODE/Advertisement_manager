from nicegui import ui 

def show_home_page():
   with ui.grid(columns=3).classes("w-screen h-screen justify-center p-8 gap-12 mx-8 items-start "):
        with ui.column().classes("w-72 items-center"):
            ui.image("Assets/furniture-5966893_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xl transition-transform duration-300 hover:scale-110")
            ui.label("single sofa").classes("mt-4 text-4xl font-semibold")
            ui.label("price:ghc 1000").classes("text-gray-700 text-xl shadow-xl")
            ui.button("view")

        with ui.column().classes("w-72 items-center"):
            ui.image("Assets/the-last-shirt-1510597_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xl transition-transform duration-300 hover:scale-110")
            ui.label("Euro Shirt").classes("mt-4 text-4xl font-semibold")
            ui.label("price:ghc 150").classes("text-gray-700 text-xl shadow-xl")
            ui.button("view")        
        with ui.column().classes("w-72 items-center"):
            ui.image("Assets/fashion-6203956_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xltransition-transform duration-300 hover:scale-110")
            ui.label("Gown").classes("mt-4 text-4xl font-semibold")
            ui.label("price:ghc 5000").classes("text-gray-700 text-xl shadow-xl")
            ui.button("view")
        with ui.column().classes("w-72 items-center"):
            ui.image("Assets/water-bottle-898332_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xl transition-transform duration-300 hover:scale-110")
            ui.label("Water-bottle").classes("mt-4 text-4xl font-semibold")
            ui.label("price:ghc 50").classes("text-gray-700 text-xl shadow-xl")
            ui.button("view")  
        with ui.column().classes("w-72 items-center"):
            ui.image("Assets/travel-bag-4326732_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xl transition-transform duration-300 hover:scale-110")
            ui.label("Travel Bag").classes("mt-4 text-4xl font-semibold")
            ui.label("price:ghc 700").classes("text-gray-700 text-xl shadow-xl")
            ui.button("view")    
        with ui.column().classes("w-72 items-center"):
            ui.image("Assets/vehicle-2132360_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xl transition-transform duration-300 hover:scale-110")
            ui.label("1987 Vintage car").classes("mt-4 text-4xl font-semibold")
            ui.label("price:ghc 3000000").classes("text-gray-700 text-xl shadow-xl")
            ui.button("view")    
        with ui.column().classes("w-72 items-center"):
            ui.image("Assets/bag-1052370_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xl transition-transform duration-300 hover:scale-110")
            ui.label("Ladies bag").classes("mt-4 text-4xl font-semibold")
            ui.label("price:ghc 400").classes("text-gray-700 text-xl shadow-xl")
            ui.button("view")    
        with ui.column().classes("w-72 items-center"):
            ui.image("Assets/chairs-2181960_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xl transition-transform duration-300 hover:scale-110")
            ui.label("Dinning table set").classes("mt-4 text-4xl font-semibold")
            ui.label("price:ghc 3000").classes("text-gray-700 text-xl shadow-xl")
            ui.button("view")    
        with ui.column().classes("w-72 items-center"):
            ui.image("Assets/mug-5161566_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xl transition-transform duration-300 hover:scale-110")
            ui.label("Mug").classes("mt-4 text-4xl font-semibold")
            ui.label("price:ghc 80").classes("text-gray-700 text-xl shadow-xl")
            ui.button("view")    
                                    