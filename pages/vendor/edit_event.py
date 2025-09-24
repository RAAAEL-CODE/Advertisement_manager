from nicegui import ui, app
import requests
import traceback
import json
from components.sidebar import show_sidebar

from components.sidebar import show_sidebar
base_url = 'https://advertisement-api-0myf.onrender.com'

# A global variable to hold the content of the uploaded file.
flyer_content = None

# API HELPERS 
def get_advert(advert_id):
    """Fetches a single advert by ID from the API."""
    try:
        response = requests.get(f'{base_url}/adverts/{advert_id}')
        response.raise_for_status()
        return response.json().get('data', {})
    except requests.exceptions.RequestException as e:
        ui.notify(f'Failed to fetch advert: {e}', type='negative')
        print(f"Error fetching advert: {e}")
        return None

def update_event(advert_id, data, files=None):
    """
    Updates an existing advert via the API using a PUT request.
    This requires sending all advert data, including unchanged fields.
    """
    url = f'{base_url}/adverts/{advert_id}'
    try:
        response = requests.put(url, data=data, files=files)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        ui.notify(f'Update failed: {e}', type='negative')
        print(f"Error updating event: {e}")
        traceback.print_exc()
        return None
        

#  Creating a handler for the upload
def handle_flyer_upload(e):
    """
    Handles the file upload event, storing the file content.
    """
    global flyer_content
    flyer_content = ('flyer.jpg', e.content.read(), 'image/jpeg')
    ui.notify('File uploaded successfully', type='positive')

# --- UI PAGES ---
@ui.page("/vendor/edit_event")
def show_edit_event_page(advert_id):
    show_sidebar()
    
    """Displays the form to edit an existing advert."""
    global flyer_content
    flyer_content = None
    
    # Fetch the advert data using the ID from the URL
    ad = get_advert(advert_id)
    if not ad:
        ui.notify("Advert not found.", type="negative")
        # In a real app, you might want to redirect back to the home page
        return

    with ui.row().classes("w-full"):
        with ui.column().classes("w-[20%]"):
            pass
        with ui.column().classes("w-[80%]"):
            with ui.column().classes('max-w-2xl mx-auto mt-12 p-8 rounded-2xl shadow-2xl bg-white space-y-6') as edit_page:
                ui.label(f'EDIT ADVERT: {ad.get("title")}').classes('font-extrabold text-3xl text-center text-gray-800')

                title = ui.input('Title', value=ad.get('title')).props('outlined').classes('w-full')
                description = ui.textarea('Item Description', value=ad.get('description')).props('outlined').classes('w-full')
                price = ui.number('Price', value=ad.get('price')).props('outlined').classes('w-full')
                categories = ui.select(
                    ['Clothing', 'Tumblers', 'Cars', 'Furniture', 'Bags'], value=ad.get('category')
                ).props('outlined').classes('w-full')

                ui.label('Upload new image (optional)').classes('font-medium text-gray-700')
                flyer = ui.upload(on_upload=handle_flyer_upload).classes('w-full rounded-lg border border-dashed border-gray-400 p-4').props("color=black")

                def save_changes():
                    """Saves the changes to the advert by calling the update API."""
                    global flyer_content
                    
                    # The API expects all fields to be present, so we fetch the original data
                    # and only update the fields that have been changed.
                    current_ad = get_advert(ad.get('id'))
                    if not current_ad:
                        ui.notify("Original advert not found. Cannot save changes.", type="negative")
                        return

                    updated_data = {
                        'title': title.value,
                        'description': description.value,
                        'price': price.value,
                        'category': categories.value,
                    }

                    # Create the final data payload by merging the old and new data.
                    data_to_send = current_ad.copy()
                    data_to_send.update(updated_data)

                    # Check if any values have actually changed before making the API call
                    has_changed = any(str(updated_data.get(key)) != str(current_ad.get(key)) for key in updated_data) or flyer_content is not None
                    
                    if not has_changed:
                        ui.notify('No changes to save.', type='info')
                        return

                    # Ensure all data values are strings for the form-data payload
                    data_to_send = {k: str(v) for k, v in data_to_send.items()}

                    response = update_event(ad.get('id'), data=data_to_send, files={'flyer': flyer_content} if flyer_content else None)
                    
                    if response and response.status_code in (200, 201):
                        ui.notify('Ad updated successfully!', type='positive')
                        ui.navigate.to('/')
                    elif response:
                        ui.notify(f'Update failed: {response.status_code} - {response.text}', type='negative')
                    
                    flyer_content = None

                ui.button('Save Changes', on_click=save_changes).classes('w-full mt-4 bg-green-500 hover:bg-green-600').props("color=black")
                ui.button('Cancel', on_click=lambda: ui.navigate.to('/')).props('flat').classes('w-full mt-2 text-gray-600').props("color=black")
