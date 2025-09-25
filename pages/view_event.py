from nicegui import ui, run, app # <-- Must import 'app' for storage access
import requests
from utils.api import base_url


# Helper function to run the blocking DELETE request with a token
def _run_delete_advert(url, token):
    """Executes the DELETE request with Authorization header in a separate thread."""
    # The server expects the token to be sent here
    return requests.delete(
        url,
        headers={"Authorization": f"Bearer {token}"},
    )


@ui.page('/view_event/{id}')
def show_view_page(id: int):
    # Fetch data for the advert
    response = requests.get(f"{base_url}/adverts/{id}")
    # Handle case where advert might not exist (e.g., 404)
    if response.status_code != 200:
        ui.notify(f"Could not load advert: {response.status_code}", type="negative")
        ui.navigate.to('/')
        return
        
    advert = response.json()["data"]

    # This async function will handle the deletion
    async def delete_advert():
        token = app.storage.user.get("access_token")
        
        if not token:
            ui.notify("Error: Not logged in or missing token.", type="negative")
            return

        _delete_url = f"{base_url}/adverts/{id}"

        # Use run.io_bound to execute the blocking requests.delete call, passing the token
        response = await run.io_bound(_run_delete_advert, _delete_url, token)
        
        if response.status_code == 200:
            ui.notify("Advert deleted successfully.", type="positive")
            # Navigate to the home page after successful deletion
            ui.navigate.to('/')
        elif response.status_code == 403:
             # Specific message for 403 (Forbidden/Not Authorized)
            ui.notify("Error 403: Forbidden. You do not have permission to delete this advert.", type="negative")
        else:
            ui.notify(f"Failed to delete advert: {response.status_code}", type="negative")

    with ui.card().classes("w-[40rem] h-1/2 sm:w-[50%] md:w-[30%] lg:w-[60%] mx-auto p-6 bg-white rounde-xl shadow-lg mt-24"):
        ui.image(advert["flyer"]).classes("w-2/3 h-full rounded-lg mb-4 shadow-xl transition-transform duration-300 hover:scale-110")
        ui.label(advert["title"]).classes("text-xl font-semibold")
        # Ensure string formatting for price uses the correct key
        ui.label(f"price:ghc {advert['price']}").classes("text-gray-700 text-xl shadow-xl") 
        ui.label(f"Category: {advert['category']}").classes("text-xl")
        ui.label(f'Description: {advert["description"]}').classes("text-grey-600 text-xl")

        with ui.grid(columns=2).classes("items-center justify-center self-center"): 
            ui.button('Exit', on_click=lambda: ui.navigate.to('/')).classes("bg-black w-[200px] text-white px-4 py-2 rounded-lg self-center")
           