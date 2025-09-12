
from nicegui import ui, events
import requests
from utils.api import base_url

flyer_content = None

def edit_event(data, files):
    response = requests.post(f'{base_url}/adverts/{'adverts_id'}', data=data, files=files)
    print(response.json())
    return response

def handle_flyer_upload(e: events.UploadEventArguments):
    global flyer_content
    flyer_content = ('flyer.jpg', e.content.read(), 'image/jpeg')
    ui.notify('File uploaded successfully')

def show_edit_event_page():
    with ui.column().classes(
        'max-w-2xl mx-auto mt-24 p-8 rounded-2xl shadow-2xl bg-white space-y-6'):
        
        ui.label('EDIT ADVERT HERE').classes(
            'font-extrabold text-4xl tracking-wide text-center text-gray-800')

        title = ui.input('Title').props('outlined').classes('w-full')
        description = ui.textarea('Item Description').props('outlined').classes('w-full')
        price = ui.number('Price').props('outlined').classes('w-full')

        ui.label('Categories').classes('font-medium text-gray-700')
        categories = ui.select(
            ['CLOTHINGS', 'TUMBLERS', 'CARS', 'FURNITURE']
        ).props('outlined').classes('w-full')

        ui.label('Upload image').classes('font-medium text-gray-700')
        flyer = ui.upload(on_upload=handle_flyer_upload).classes(
            'w-full rounded-lg border border-dashed border-gray-400 p-4')

        def submit():
            global flyer_content
            ad_data = {
                'title': title.value,
                'description': description.value,
                'price': price.value,
                'category': categories.value,
            }
            response = edit_event(ad_data, files={'flyer': flyer_content})
            if response.status_code == 200:
                ui.notify('Ad submitted successfully!')
            else:
                ui.notify(f'Failed: {response.text}')

        ui.button('Submit', on_click=submit).classes(
            'mt-6 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 px-6 rounded-xl shadow-md w-full'
        )

        def delete():
            ui.notify('Deleted Successfully')

        ui.button('Delete', on_click=delete).classes(
            'mt-3 bg-red-600 hover:bg-red-700 text-white font-semibold py-3 px-6 rounded-xl shadow-md w-full'
        )
