from nicegui import ui, app, run # ADDED 'run'
import requests
import traceback
import json
from components.sidebar import show_sidebar

base_url = 'https://advertisement-api-0myf.onrender.com'

# A global variable to hold the content of the uploaded file.
flyer_content = None

# --- API HELPERS (Synchronous) ---

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

# NEW HELPER: Synchronous function to execute the PUT request securely
def _run_update_event(advert_id, data, files, token):
    """Executes the synchronous PUT request with authorization headers."""
    url = f'{base_url}/adverts/{advert_id}'
    headers = {"Authorization": f"Bearer {token}"}
    return requests.put(url, data=data, files=files, headers=headers)

# NEW WRAPPER: Asynchronous function to handle thread and token logic
async def update_event_async(advert_id, data, files=None):
    token = app.storage.user.get("access_token") # CRITICAL FIX: Get token
    if not token:
        ui.notify("Authentication Error: Please log in again.", type='negative')
        return None

    try:
        response = await run.io_bound(_run_update_event, advert_id, data, files, token)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as e:
        error_detail = e.response.json().get('detail', e.response.text) if e.response.content else str(e)
        ui.notify(f'Update failed: {e.response.status_code} - {error_detail}', type='negative')
        print(f"API Update Error ({e.response.status_code}): {error_detail}")
        return None
    except requests.exceptions.RequestException as e:
        ui.notify(f'Update failed: {e}', type='negative')
        print(f"Error updating event: {e}")
        traceback.print_exc()
        return None


# Creating a handler for the upload
def handle_flyer_upload(e):
    """Handles the file upload event, storing the file content."""
    global flyer_content
    flyer_content = (e.name, e.content.read(), e.type) 
    ui.notify('File uploaded successfully', type='positive')

# --- UI PAGES ---
@ui.page("/vendor/edit_event")
def show_edit_event_page(advert_id):
    global flyer_content # FIX: Must be at the very top
    
    show_sidebar()
    
    """Displays the form to edit an existing advert."""
    flyer_content = None # Reset flyer content state
    
    # Fetch the advert data using the ID from the URL
    ad = get_advert(advert_id)
    if not ad:
        ui.notify("Advert not found.", type="negative")
        return

    # CRITICAL FIX: Make save_changes ASYNC
    async def save_changes():
        """Saves the changes to the advert by calling the update API."""
        global flyer_content # FIX: Must be at the very top of this function
        
        # Get element values here, as they are defined in the outer scope
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

        data_to_send = current_ad.copy()
        data_to_send.pop('id', None) 
        data_to_send.pop('owner_id', None)
        data_to_send.pop('views', None)
        data_to_send.update(updated_data)

        has_changed = any(str(updated_data.get(key)) != str(current_ad.get(key)) for key in updated_data) or flyer_content is not None
        
        if not has_changed:
            ui.notify('No changes to save.', type='info')
            return

        data_to_send_strings = {k: str(v) for k, v in data_to_send.items()}
        files_to_send = {'flyer': flyer_content} if flyer_content else None

        # CRITICAL FIX: Use the async wrapper
        response = await update_event_async(
            ad.get('id'), 
            data=data_to_send_strings, 
            files=files_to_send
        )
        
        if response and response.status_code in (200, 201):
            ui.notify('Ad updated successfully!', type='positive')
            ui.navigate.to('/vendor/dashboard') 
            flyer_content = None


    # --- ORIGINAL UI LAYOUT RESTORED ---
    with ui.row().classes("w-full"):
        with ui.column().classes("w-[20%]"):
            pass
        with ui.column().classes("w-[80%]"):
            with ui.column().classes('w-[40rem] mx-auto mt-12 p-8 rounded-2xl shadow-2xl bg-white space-y-6') as edit_page:
                ui.label(f'EDIT ADVERT: {ad.get("title")}').classes('font-extrabold text-3xl text-center text-gray-800')

                # UI Element Definitions (Kept in Original Layout Position)
                title = ui.input('Title', value=ad.get('title')).props('outlined').classes('w-full')
                description = ui.textarea('Item Description', value=ad.get('description')).props('outlined').classes('w-full')
                price = ui.number('Price', value=ad.get('price')).props('outlined').classes('w-full')
                categories = ui.select(
                    ['Clothing', 'Tumblers', 'Cars', 'Furniture', 'Bags'], value=ad.get('category')
                ).props('outlined').classes('w-full')

                ui.label('Upload new image (optional)').classes('font-medium text-gray-700')
                flyer = ui.upload(on_upload=handle_flyer_upload).classes('w-full rounded-lg border border-dashed border-gray-400 p-4').props("color=black")

                # The save_changes function definition relies on the elements above
                ui.button('Save Changes', on_click=save_changes).classes('w-full mt-4 bg-green-500 hover:bg-green-600').props("color=black")
                ui.button('Cancel', on_click=lambda: ui.navigate.to('/vendor/dashboard')).props('flat').classes('w-full mt-2 text-gray-600').props("color=black")