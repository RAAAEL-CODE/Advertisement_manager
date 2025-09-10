from nicegui import ui 

def show_edit_event_page():
    with ui.column().classes('max-w-2xl mx-auto rounded-lg shadow-xl w-full mt-24'):
        ui.label ('EDIT ADVERT').classes('text-bold mb-6  text-3xl tracking-wider text-center self-center')
        ui.input('Title').props('outlined').classes('w-full')
        ui.textarea('Item Description').props('outlined').classes('w-full')
        ui.number('Price').props('outlined').classes('w-full')
        ui.label('Categories').classes('font-light mb-2')
        ui.select(['CLOTHINGS','TUMBLERS','CARS', 'FURNITURE']).classes("w-[670px]").props('outlined')
        ui.label('Upload image').classes('font-light mb-2')
        ui.upload(on_upload=lambda e: ui.notify(f'Uploaded'),
        on_rejected=lambda: ui.notify('Rejected!'),
        max_file_size=5_000_000).classes('w-[670px]')
    
        def submit():
            ui.notify(f'Add Submitted Successfully')
    ui.button('Submit', on_click=submit).classes('mt-4 bg-black text-white w-[200px] self-center')    