# from nicegui import ui, run, app
# import requests
# from components.sidebar import show_sidebar
# from utils.api import base_url # Assumed path for API root URL
# from typing import List, Dict, Any # For type hinting

# # --- Helper Function for API Call (Runs in a separate thread) ---
# def _run_get_my_adverts(url, token):
#     """Executes the authenticated GET request for vendor's adverts."""
#     # This runs the synchronous requests call off the main thread
#     return requests.get(
#         url,
#         headers={"Authorization": f"Bearer {token}"},
#     )

# # --- Main Dashboard Page (ASYNC for I/O operations) ---
# @ui.page("/vendor/dashboard")
# async def vendor_dashboard():
#     show_sidebar()

#     # --- Data Fetching Logic ---
#     async def get_initial_data():
#         token = app.storage.user.get("access_token")
#         if not token:
#             ui.notify("Authentication Error: Please log in.", type="negative")
#             # Return defaults on failure
#             return [], 0, 0, {}, [], ([], [])

#         # FIX: Using the confirmed correct API endpoint: /adverts/me
#         _my_adverts_url = f"{base_url}/adverts/me" 
        
#         # Execute the authenticated GET request using run.io_bound
#         response = await run.io_bound(_run_get_my_adverts, _my_adverts_url, token)
        
#         if response.status_code == 200:
#             vendor_adverts = response.json().get("data", [])
            
#             # --- Dynamic Calculations ---
#             total_adverts = len(vendor_adverts)
#             total_views = sum(int(a.get('views', 0)) for a in vendor_adverts)
            
#             category_counts = {}
#             for advert in vendor_adverts:
#                 cat = advert.get('category', 'Uncategorized')
#                 category_counts[cat] = category_counts.get(cat, 0) + 1
                
#             pie_data = [{'value': count, 'name': cat} for cat, count in category_counts.items()]
            
#             bar_labels = [a.get('title', f"Advert {a.get('id', 'N/A')}") for a in vendor_adverts]
#             bar_views = [int(a.get('views', 0)) for a in vendor_adverts]

#             return vendor_adverts, total_adverts, total_views, category_counts, pie_data, (bar_labels, bar_views)

#         else:
#             # Notify of failure, showing the error code and message
#             error_message = response.text if response.text else "Unknown error"
#             ui.notify(f"Failed to fetch adverts: {response.status_code} - {error_message}", type="negative")
#             print(f"API Error ({response.status_code}): {error_message}")
#             return [], 0, 0, {}, [], ([], [])

#     # Call the async data fetching function using await
#     vendor_adverts, total_adverts, total_views, category_counts, pie_data, bar_data_tuple = await get_initial_data()
    
#     bar_labels, bar_views = bar_data_tuple if bar_data_tuple else ([], [])
#     categories = len(category_counts)
    
#     # --- UI Layout (Uses dynamic variables) ---
#     with ui.column().classes('w-full h-screen p-6 space-y-6'):
#         # Header with button
#         with ui.row().classes('justify-between items-center w-full'):
#             ui.label('Welcome, RAEEL-Vendor!').classes('text-3xl font-bold text-gray-800')
#             ui.button(
#                 '➕ Post New Advert',
#                 on_click=lambda: ui.navigate.to('/vendor/new_advert'),
#             ).classes(
#                 'bg-black text-white ml-auto px-4 py-2 rounded-lg hover:bg-gray-800 transition duration-200'
#             )

#         # Summary cards (Uses integrated data)
#         with ui.row().classes('w-full gap-6'):
#             for label, value in [
#                 ('Total Adverts', str(total_adverts)),
#                 ('Categories', str(categories)),
#                 ('Total Views', f"{total_views:,}"),
#             ]:
#                 with ui.card().classes('w-1/3 p-4'):
#                     ui.label(label).classes('text-lg text-gray-600')
#                     ui.label(value).classes('text-3xl font-bold')

#         # Analytics
#         ui.label('Analytics').classes('text-2xl font-bold text-gray-800')

#         # Pie Chart: Adverts by Category (Integrated data)
#         with ui.card().classes('w-full h-96 p-4'):
#             ui.echart({
#                 'title': {'text': 'Adverts by Category', 'left': 'center'},
#                 'tooltip': {'trigger': 'item'},
#                 'legend': {'orient': 'vertical', 'left': 'left'},
#                 'series': [{
#                     'name': 'Adverts',
#                     'type': 'pie',
#                     'radius': '50%',
#                     'center':['40%','50%'],
#                     # DYNAMIC DATA
#                     'data': pie_data,
#                     'emphasis': {
#                         'itemStyle': {
#                             'shadowBlur': 10,
#                             'shadowOffsetX': 0,
#                             'shadowColor': 'rgba(0, 0, 0, 0.5)',
#                         }
#                     },
#                 }],
#             }).style('width:100%; height:100%;')

#         # Bar Chart: Views per Advert (Integrated data)
#         with ui.card().classes('w-full h-96 p-4'):
#             ui.echart({
#                 'title': {'text': 'Views per Advert', 'left': 'center'},
#                 'tooltip': {'trigger': 'axis'},
#                 # DYNAMIC DATA
#                 'xAxis': {'type': 'category', 'data': bar_labels},
#                 'yAxis': {'type': 'value'},
#                 'series': [{
#                     # DYNAMIC DATA
#                     'data': bar_views,
#                     'type': 'bar',
#                     'barWidth': '50%',
#                     'itemStyle': {'color': '#1f2937'},
#                 }],
#             }).style('width:100%; height:100%;')

#         # Adverts list
#         ui.label('My Adverts').classes('text-2xl font-bold text-gray-800')

#         # Function to create an individual advert card
#         def advert_card(title, category, views, advert_id, flyer_url):
#             with ui.card().classes('w-72 p-4'):
#                 ui.image(flyer_url).classes('w-full h-32 object-cover rounded mb-4')
#                 ui.label(title).classes('text-lg font-semibold text-gray-800 truncate')
#                 ui.label(f'Category: {category}').classes('text-sm text-gray-600')
#                 ui.label(f'Views: {views}').classes('text-sm text-gray-600 mb-2')
#                 with ui.row().classes('justify-between w-full'):
#                     # Ensure advert_id is used for navigation
#                     ui.button(
#                         'Edit',
#                         on_click=lambda: ui.navigate.to(f"/vendor/edit_event?advert_id={advert_id}")
#                     ).classes('bg-black text-white px-3 py-1 rounded hover:bg-gray-800')
                    
#                     ui.button('Delete', on_click=lambda: ui.notify(f"Delete logic initiated for advert {advert_id}")) \
#                         .classes('bg-red-600 text-white px-3 py-1 rounded hover:bg-red-700')

#         # Dynamic Advert Card Generation
#         with ui.row().classes('w-full gap-6 flex-wrap'):
#             if vendor_adverts:
#                 for advert in vendor_adverts:
#                     advert_card(
#                         title=advert.get('title', 'No Title'),
#                         category=advert.get('category', 'N/A'),
#                         views=advert.get('views', 0),
#                         advert_id=advert.get('id'),
#                         flyer_url=advert.get('flyer', 'https://via.placeholder.com/300x150')
#                     )
#             else:
#                 ui.label("You have no active adverts.").classes("text-lg text-gray-500 w-full text-center")
from nicegui import ui, run, app
import requests
from components.sidebar import show_sidebar
from utils.api import base_url # ASSUMED: This provides the base URL for your API
from typing import List, Dict, Any 

# --- Helper Function for API Call (Runs in a separate thread) ---
def _run_get_my_adverts(url, token):
    """Executes the authenticated GET request for vendor's adverts."""
    # We use the synchronous requests library inside this function
    return requests.get(
        url,
        headers={"Authorization": f"Bearer {token}"},
    )

# --- Main Dashboard Page (ASYNC for I/O operations) ---
@ui.page("/vendor/dashboard")
async def vendor_dashboard(): # FIX 1: Make the page function async
    show_sidebar()

    # --- Data Fetching Logic ---
    async def get_initial_data():
        token = app.storage.user.get("access_token")
        if not token:
            ui.notify("Authentication Error: Please log in.", type="negative")
            return [], 0, 0, {}, [], ([], [])

        # FIX 2: Use the correct backend endpoint /adverts/me (confirmed by API docs)
        _my_adverts_url = f"{base_url}/adverts/user/me" 
        
        # Execute the authenticated GET request using run.io_bound
        response = await run.io_bound(_run_get_my_adverts, _my_adverts_url, token)
        
        if response.status_code == 200:
            vendor_adverts = response.json().get("data", [])
            
            # --- Dynamic Calculations ---
            total_adverts = len(vendor_adverts)
            # Ensure 'views' is treated as an integer for summation
            total_views = sum(int(a.get('views', 0)) for a in vendor_adverts)
            
            category_counts = {}
            for advert in vendor_adverts:
                cat = advert.get('category', 'Uncategorized')
                category_counts[cat] = category_counts.get(cat, 0) + 1
                
            pie_data = [{'value': count, 'name': cat} for cat, count in category_counts.items()]
            
            bar_labels = [a.get('title', f"Advert {a.get('id', 'N/A')}") for a in vendor_adverts]
            bar_views = [int(a.get('views', 0)) for a in vendor_adverts]

            return vendor_adverts, total_adverts, total_views, category_counts, pie_data, (bar_labels, bar_views)

        else:
            # Handle API failure, which was previously the 422 error
            error_message = response.text if response.text else "Unknown error"
            ui.notify(f"Failed to fetch adverts: {response.status_code} - {error_message}", type="negative")
            print(f"API Error ({response.status_code}): {error_message}")
            return [], 0, 0, {}, [], ([], [])

    # Call the async data fetching function using await
    vendor_adverts, total_adverts, total_views, category_counts, pie_data, bar_data_tuple = await get_initial_data()
    
    bar_labels, bar_views = bar_data_tuple if bar_data_tuple else ([], [])
    categories = len(category_counts)
    
    # --- UI Layout (Uses dynamic variables) ---
    with ui.column().classes('w-full h-screen p-6 space-y-6'):
        # Header with button
        with ui.row().classes('justify-between items-center w-full'):
            ui.label('Welcome, RAEEL-Vendor!').classes('text-3xl font-bold text-gray-800')
            ui.button(
                '➕ Post New Advert',
                on_click=lambda: ui.navigate.to('/vendor/new_advert'),
            ).classes(
                'bg-black text-white ml-auto px-4 py-2 rounded-lg hover:bg-gray-800 transition duration-200'
            )

        # Summary cards (Uses integrated data)
        with ui.row().classes('w-full gap-6'):
            for label, value in [
                ('Total Adverts', str(total_adverts)),
                ('Categories', str(categories)),
                ('Total Views', f"{total_views:,}"), # Add comma formatting
            ]:
                with ui.card().classes('w-1/3 p-4'):
                    ui.label(label).classes('text-lg text-gray-600')
                    ui.label(value).classes('text-3xl font-bold')

        # Analytics
        ui.label('Analytics').classes('text-2xl font-bold text-gray-800')

        # Pie Chart: Adverts by Category (Integrated data)
        with ui.card().classes('w-full h-96 p-4'):
            ui.echart({
                'title': {'text': 'Adverts by Category', 'left': 'center'},
                'tooltip': {'trigger': 'item'},
                'legend': {'orient': 'vertical', 'left': 'left'},
                'series': [{
                    'name': 'Adverts',
                    'type': 'pie',
                    'radius': '50%',
                    'center':['40%','50%'],
                    'data': pie_data, # DYNAMIC DATA
                    'emphasis': {
                        'itemStyle': {
                            'shadowBlur': 10,
                            'shadowOffsetX': 0,
                            'shadowColor': 'rgba(0, 0, 0, 0.5)',
                        }
                    },
                }],
            }).style('width:100%; height:100%;')

        # Bar Chart: Views per Advert (Integrated data)
        with ui.card().classes('w-full h-96 p-4'):
            ui.echart({
                'title': {'text': 'Views per Advert', 'left': 'center'},
                'tooltip': {'trigger': 'axis'},
                'xAxis': {'type': 'category', 'data': bar_labels}, # DYNAMIC DATA
                'yAxis': {'type': 'value'},
                'series': [{
                    'data': bar_views, # DYNAMIC DATA
                    'type': 'bar',
                    'barWidth': '50%',
                    'itemStyle': {'color': '#1f2937'},
                }],
            }).style('width:100%; height:100%;')

        # Adverts list
        ui.label('My Adverts').classes('text-2xl font-bold text-gray-800')

        # Function to create an individual advert card
        def advert_card(title, category, views, advert_id, flyer_url):
            with ui.card().classes('w-72 p-4'):
                # Assumes 'flyer' field in API returns a valid URL, else uses placeholder
                ui.image(flyer_url).classes('w-full h-32 object-cover rounded mb-4')
                ui.label(title).classes('text-lg font-semibold text-gray-800 truncate')
                ui.label(f'Category: {category}').classes('text-sm text-gray-600')
                ui.label(f'Views: {views}').classes('text-sm text-gray-600 mb-2')
                with ui.row().classes('justify-between w-full'):
                    # CORRECTED LINE
                    ui.button(
                    'Edit',
                    on_click=lambda id=advert_id: ui.navigate.to(f"/vendor/edit_event?advert_id={id}") 
                ).classes('bg-black text-white px-3 py-1 rounded hover:bg-gray-800')
                    
                    ui.button('Delete', on_click=lambda: ui.notify(f"Delete logic initiated for advert {advert_id}")) \
                        .classes('bg-red-600 text-white px-3 py-1 rounded hover:bg-red-700')

        # Dynamic Advert Card Generation
        with ui.row().classes('w-full gap-6 flex-wrap'):
            if vendor_adverts:
                for advert in vendor_adverts:
                    advert_card(
                        title=advert.get('title', 'No Title'),
                        category=advert.get('category', 'N/A'),
                        views=advert.get('views', 0),
                        advert_id=advert.get('id'),
                        flyer_url=advert.get('flyer', 'https://via.placeholder.com/300x150')
                    )
            else:
                ui.label("You have no active adverts.").classes("text-lg text-gray-500 w-full text-center")