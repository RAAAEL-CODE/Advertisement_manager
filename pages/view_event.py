from nicegui import ui 

def show_view_page():
    goods =["funiture"]
    with ui.column():
        ui.select(label="category", options=["All" "funiture"], on_change=lambda e: filter_goods(e.value))
        for good in goods:
            with ui.column():
                ui.image("Assets/the-last-shirt-1510597_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xl transition-transform duration-300 hover:scale-110")
                ui.label("Euro Shirt").classes("text-xl font-semibold")
                ui.label("price:ghc 150").classes("text-gray-700 text-xl shadow-xl")
                ui.label("Description: A single mordern sofa with plush cushions-Elastic silky fiber fabric. Available in different colors. visit shop for a 50% discount ").classes("items-center")
def filter_goods(category):
    pass                
            
    ui.label ('This is the view page')