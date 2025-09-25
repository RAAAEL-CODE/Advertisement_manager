from nicegui import ui
from components.sidebar import show_sidebar

@ui.page("/support")
def support_page():
    show_sidebar()
    with ui.column().classes('w-full h-screen p-6 space-y-6'):
        ui.label('Support & Help').classes('text-3xl font-bold text-gray-800')

        # Support Form
        with ui.card().classes('w-full max-w-lg p-6 mx-auto'):
            ui.label('Submit a Support Request').classes('text-xl font-semibold mb-4')
            
            ui.input('Your Name', placeholder='Enter your name').classes('w-full mb-4')
            ui.input('Email', placeholder='Enter your email').classes('w-full mb-4')
            
            ui.textarea('Describe your issue', placeholder='Please provide a detailed description of your problem...').classes('w-full mb-4')
            
            ui.button('Submit Request', on_click=lambda: ui.notify('Your request has been submitted!', type='positive')).classes('w-full bg-black text-white px-4 py-2 rounded-lg hover:bg-gray-800 transition duration-200')
