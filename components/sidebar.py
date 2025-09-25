from nicegui import ui, events
from nicegui.page import page

# This is the base URL for the DiceBear AI avatar generator.
AVATAR_API_URL = "https://api.dicebear.com/7.x/adventurer/svg?seed=VendorName"

def show_sidebar():
    """A reusable sidebar component with navigation links and profile info."""
    with ui.left_drawer(value=True, bordered=True).classes('bg-[#f8f9fa] w-64'):
        with ui.column().classes('items-center p-4 border-b gap-2'):
            # Generate a unique avatar URL for the "Vendor Name".
        
            avatar_url = f'{AVATAR_API_URL}?seed={"Vendor Name"}'
            
            uploaded_picture = ui.image(avatar_url).classes(
                'w-24 h-24 rounded-full shadow-lg border-4 border-white '
                'transition-transform duration-300 hover:scale-105 hover:shadow-2xl'
            )
            ui.label('Vendor Name').classes('text-base font-semibold mt-2')
            ui.label('Advertiser').classes('text-sm text-gray-600')

        # Navigation Links
        # All links are inside this single drawer context.
        ui.link('Dashboard', '/vendor/dashboard').classes('flex items-center p-3 hover:bg-gray-200 text-black rounded-lg').props('style="text-decoration: none;"')
        ui.link('Create New Advert', '/vendor/add_event').classes('flex items-center p-3 hover:bg-gray-200 text-black rounded-lg').props('style="text-decoration: none;"')
        #ui.link('Payments / Billing', '/billing').classes('flex items-center text-black p-3 hover:bg-gray-200 rounded-lg').props('style="text-decoration: none;"')
        ui.link('Payments / Billing', '/vendor/billing').classes('flex items-center text-black p-3 hover:bg-gray-200 rounded-lg').props('style="text-decoration: none;"')
        ui.separator()
        ui.link('Notifications', '/notifications').classes('flex items-center p-3 hover:bg-gray-200 text-black rounded-lg').props('style="text-decoration: none;"')
        ui.link('Support / Help', '/support').classes('flex items-center text-black p-3 hover:bg-gray-200 rounded-lg').props('style="text-decoration: none;"')
        ui.separator()
        ui.link('Home', '/').classes('flex items-center p-3 text-black hover:bg-gray-200 rounded-lg').props('style="text-decoration: none;"')
        #ui.link('Logout', '/logout').classes('flex items-center text-black p-3 text-red-600 hover:bg-red-100 rounded-lg').props('style="text-decoration: none;"')
        def logout():
            ui.navigate.to('/signin')

        ui.button('Logout', on_click=logout).classes('flex items-center text-black p-3 text-red-600 hover:bg-red-100 rounded-lg w-full').props('flat style="text-decoration: none;"')