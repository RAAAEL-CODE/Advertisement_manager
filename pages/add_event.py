from nicegui import ui 
import requests
from utils.api import base_url


def add_event(data):
    response=requests.post(f'{base_url}/adverts', data)
    print(response.json())

def show_add_event_page():
    flyer_content=None

    def handle_flyer_upload(e):
        global flyer_content
        flyer_content = {'name': e.name, 'content': e.content.read(), 'type':e.type}
        ui.notify(f'uploaded')


    with ui.column().classes(
        'max-w-2xl mx-auto mt-24 p-8 rounded-2xl shadow-2xl bg-white space-y-6'):
        # Title
        ui.label('CREATE A NEW ADVERT').classes(
            'font-extrabold text-4xl tracking-wide text-center text-gray-800')

        # Inputs
        title = ui.input('Title').props('outlined').classes(
            'w-full rounded-lg border-gray-300 focus:ring-2 focus:ring-indigo-500'
        )

        description = ui.textarea('Item Description').props('outlined').classes(
            'w-full rounded-lg border-gray-300 focus:ring-2 focus:ring-indigo-500'
        )

        price = ui.number('Price').props('outlined').classes(
            'w-full rounded-lg border-gray-300 focus:ring-2 focus:ring-indigo-500'
        )

        # Categories
        ui.label('Categories').classes('font-medium text-gray-700')
        categories = ui.select(
            ['CLOTHINGS', 'TUMBLERS', 'CARS', 'FURNITURE']
        ).classes("w-full rounded-lg").props('outlined')

        # Upload
        ui.label('Upload image').classes('font-medium text-gray-700')
        flyer = ui.upload(on_upload=handle_flyer_upload).classes('w-full rounded-lg border border-dashed border-gray-400 p-4')

        # Submit button
        #def submit():
            #ad_data={
                #'title':title.value,
                #'description':description.value,
                #'price':price.value,
                #'category':categories.value,
                

            #}
           # print(ad_data)
        def submit():
            ui.notify(
                f"Ad Submitted: {title.value}, {description.value}, {price.value}, {categories.value}"
            )

        ui.button('Submit', on_click=lambda:add_event({
            'title':title.value,
                'description':description.value,
                'price':price.value,
                'category':categories.value,
                'flyer': flyer_content})).classes(
            'mt-6 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 px-6 rounded-xl shadow-md w-full'
        )

        # Delete button
        def delete():
            ui.notify('Deleted Successfully')

        ui.button('Delete', on_click=delete).classes(
            'mt-3 bg-red-600 hover:bg-red-700 text-white font-semibold py-3 px-6 rounded-xl shadow-md w-full'
        )


