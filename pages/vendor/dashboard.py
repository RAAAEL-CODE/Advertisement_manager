from nicegui import ui
from components.sidebar import show_sidebar
import requests
from utils.api import base_url


def delete_advert(advert_id: str):
    """Delete an advert and refresh dashboard."""
    response = requests.delete(f"{base_url}/adverts/{advert_id}")
    if response.status_code == 200:
        ui.notify("Advert deleted successfully!", type="positive")
        ui.navigate.to("/pages/vendor/dashboard")
    else:
        ui.notify(f"Failed to delete advert: {response.status_code}", type="negative")


@ui.page("/pages/vendor/dashboard")
def vendor_dashboard():
    with ui.row().classes('w-full h-screen'):
        show_sidebar()
    
        with ui.column().classes('w-5/5 p-6 space-y-6'):

            # Header with button
            with ui.row().classes('justify-between items-center w-full'):
                ui.label('Welcome, RAEEL-Vendor!').classes('text-3xl font-bold text-gray-800')

            # Summary cards
            with ui.row().classes('w-full gap-6'):
                with ui.card().classes('w-1/3 p-4'):
                    ui.label('Total Adverts').classes('text-lg text-gray-600')
                    ui.label('12').classes('text-3xl font-bold')
                with ui.card().classes('w-1/3 p-4'):
                    ui.label('Categories').classes('text-lg text-gray-600')
                    ui.label('5').classes('text-3xl font-bold')
                with ui.card().classes('w-1/3 p-4'):
                    ui.label('Total Views').classes('text-lg text-gray-600')
                    ui.label('2,340').classes('text-3xl font-bold')

            # Analytics section
            ui.label('Analytics').classes('text-2xl font-bold text-gray-800')

            # Example: Pie Chart for Ads by Category
            ui.echart({
                'title': {'text': 'Adverts by Category', 'left': 'center'},
                'tooltip': {'trigger': 'item'},
                'legend': {'orient': 'vertical', 'left': 'left'},
                'series': [
                    {
                        'name': 'Adverts',
                        'type': 'pie',
                        'radius': '50%',
                        'data': [
                            {'value': 6, 'name': 'Electronics'},
                            {'value': 4, 'name': 'Fashion'},
                            {'value': 2, 'name': 'Furniture'},
                        ],
                    }
                ],
            }).classes('w-full h-96')

            # Adverts list
            ui.label('My Adverts').classes('text-2xl font-bold text-gray-800')

            with ui.row().classes('w-full gap-6 flex-wrap'):

                def advert_card(advert):
                    with ui.card().classes('w-72 p-4'):
                        ui.image(advert.get("flyer_url", "https://via.placeholder.com/300x150")).classes('w-full h-32 rounded mb-4')
                        ui.label(advert.get("title", "Untitled")).classes('text-lg font-semibold text-gray-800')
                        ui.label(f'Category: {advert.get("category", "N/A")}').classes('text-sm text-gray-600')
                        ui.label(f'Views: {advert.get("views", 0)}').classes('text-sm text-gray-600 mb-2')
                        with ui.row().classes('justify-between'):
                            ui.button(
                                "Edit",
                                on_click=lambda advert_id=advert["id"]: ui.navigate.to(f'/vendor/edit_event/{advert_id}')
                            ).classes("bg-black text-white px-4 py-2 rounded-lg")
                            ui.button(
                                "Delete",
                                on_click=lambda advert_id=advert["id"]: delete_advert(advert_id)
                            ).classes("bg-black text-white px-4 py-2 rounded-lg")

                # Fetch adverts dynamically from API
                response = requests.get(f"{base_url}/adverts")
                if response.status_code == 200:
                    adverts = response.json().get("data", [])
                    for ad in adverts:
                        advert_card(ad)
                else:
                    ui.label("Failed to load adverts").classes("text-red-600")
