from nicegui import ui, events
import requests
from utils.api import base_url 

# Base URL for the API
# NOTE: Replace with your actual API base URL.


# Global variable to store the uploaded flyer file
flyer_file = None

def add_event(data, files, container):
    """
    Sends a POST request to the API to create a new advert.
    """
    try:
        response = requests.post(f'{base_url}/adverts', data=data, files=files)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        ui.notify('Ad submitted successfully! 🎉', type='positive')
        print(response.json())
        # You would typically refresh the home page or add the new item here.
        # This is where you'd call a function to update the main page with the new ad.
        # Example: update_home_page_with_new_ad(response.json())
    except requests.exceptions.RequestException as e:
        ui.notify(f'Failed to submit ad: {e}', type='negative')
        print(f"Error: {e}")

def handle_flyer_upload(e: events.UploadEventArguments):
    """
    Handles the file upload event, storing the file for later submission.
    """
    global flyer_file
    flyer_file = (e.name, e.content.read(), e.type)
    ui.notify(f'Uploaded: {e.name}')

def show_add_event_page():
    """
    Displays the form for creating a new advert.
    """
    with ui.column().classes('max-w-2xl mx-auto mt-24 p-8 rounded-2xl shadow-2xl bg-white space-y-6'):
        ui.label('CREATE A NEW ADVERT').classes('font-extrabold text-4xl tracking-wide text-center text-gray-800')

        title = ui.input('Title').props('outlined').classes('w-full rounded-lg border-gray-300 focus:ring-2 focus:ring-indigo-500')
        description = ui.textarea('Item Description').props('outlined').classes('w-full rounded-lg border-gray-300 focus:ring-2 focus:ring-indigo-500')
        price = ui.number('Price').props('outlined').classes('w-full rounded-lg border-gray-300 focus:ring-2 focus:ring-indigo-500')

        # Categories
        ui.label('Categories').classes('font-medium text-gray-700')
        categories = ui.select(['CLOTHINGS', 'TUMBLERS', 'CARS', 'FURNITURE']).classes("w-full rounded-lg").props('outlined')
        #upload
        ui.label('Upload image').classes('font-medium text-gray-700')
        # Assign handle_flyer_upload to the on_upload event.
        flyer_uploader = ui.upload(on_upload=handle_flyer_upload).classes('w-full rounded-lg border border-dashed border-gray-400 p-4')

        # The submit button's on_click now properly sends data and the file.
        def submit_form():
            global flyer_file
            
            # Prepare the data dictionary.
            ad_data = {
                'title': title.value,
                'description': description.value,
                'price': price.value,
                'category': categories.value,
            }

            # Prepare the files dictionary.
            # The key 'flyer' must match the expected field name on your backend.
            files_data = {'flyer': flyer_file} if flyer_file else None

            # Call the add_event function with the prepared data and files.
            add_event(ad_data, files_data)

        ui.button('Submit', on_click=submit_form).classes('mt-6 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 px-6 rounded-xl shadow-md w-full')
        #delete button
        def delete():
            ui.notify('Deleted Successfully')

        ui.button('Delete', on_click=delete).classes('mt-3 bg-red-600 hover:bg-red-700 text-white font-semibold py-3 px-6 rounded-xl shadow-md w-full')



