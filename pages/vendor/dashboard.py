# In pages/vendor/dashboard.py
from nicegui import ui
from components.sidebar import show_sidebar

@ui.page("/vendor/dashboard")
def vendor_dashboard():
    # Correct: Call show_sidebar() at the top level of the page.
    show_sidebar()
    
    # Place the main dashboard content directly inside the page function.
    with ui.column().classes('w-full h-screen p-6 space-y-6'):
        # Header with button
        with ui.row().classes('justify-between items-center w-full'):
            ui.label('Welcome, RAEEL-Vendor!').classes('text-3xl font-bold text-gray-800')
            ui.button('➕ Post New Advert').classes(
                'bg-black text-white ml-auto px-4 py-2 rounded-lg hover:bg-gray-800 transition duration-200'
            )

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

        # Adverts list
        ui.label('My Adverts').classes('text-2xl font-bold text-gray-800')

        with ui.row().classes('w-full gap-6 flex-wrap'):

            def advert_card(title, category, views):
                with ui.card().classes('w-72 p-4'):
                    ui.image('https://via.placeholder.com/300x150').classes('w-full h-32 rounded mb-4')
                    ui.label(title).classes('text-lg font-semibold text-gray-800')
                    ui.label(f'Category: {category}').classes('text-sm text-gray-600')
                    ui.label(f'Views: {views}').classes('text-sm text-gray-600 mb-2')
                    with ui.row().classes('justify-between'):
                        ui.button('Edit').classes('bg-black text-white px-3 py-1 rounded hover:bg-gray-800')
                        ui.button('Delete').classes('bg-black text-white px-3 py-1 rounded hover:bg-gray-800')

            advert_card('Advert 1', 'Electronics', 450)
            advert_card('Advert 2', 'Fashion', 310)
            advert_card('Advert 3', 'Furniture', 120)