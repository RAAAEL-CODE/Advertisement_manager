from nicegui import ui 

def show_edit_event_page():
    ui.label ('EDIT ADVERT').classes('text-bold text-3xl tracking-wider items-center')
    Title=ui.input('Title').props('outlined').classes('w-1/2 items-center')
    Description=ui.textarea('Item Description').props('outlined').classes('w-1/2 items-center')
    Price=ui.number('Price').props('outlined').classes('w-1/2 items-center')
    ui.select(['Upload image from camera roll','Browse',]).classes("w-[670px] items-center").props('outlined')
    
    def submit():
        ui.notify(f'Add Submitted Successfully: {Title.value}')
    ui.button('Submit', on_click=submit).classes('mt-4 bg-black text-white justify-center items-center w-[200px]')    