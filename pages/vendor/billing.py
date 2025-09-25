from nicegui import ui
from components.sidebar import show_sidebar

@ui.page("/vendor/billing")
def billing_page():
    show_sidebar()
    with ui.column().classes('p-6 w-full'):
        ui.label("Payments & Billing").classes('text-3xl font-bold')
        ui.label("This is where your billing information and payment history will be displayed.").classes('text-lg text-gray-600')

        ui.card().classes('w-full p-4 mt-4').style('border-left: 5px solid #1f2937;')
        with ui.row().classes('w-full justify-between items-center'):
            ui.label("Current Plan").classes('text-xl font-semibold')
            ui.button("Upgrade Plan").classes('bg-black text-white rounded-lg px-4 py-2 hover:bg-gray-800')

        ui.separator().classes('my-4')

        with ui.column().classes('w-full space-y-4'):
            ui.label("Payment History").classes('text-xl font-semibold')
            with ui.row().classes('w-full p-2 bg-gray-100 rounded-lg justify-between items-center'):
                ui.label("Invoice #123456").classes('font-medium')
                ui.label("₵49.00").classes('font-bold text-green-600')
                ui.label("2024-09-20").classes('text-sm text-gray-500')
                ui.button("View Invoice").classes('text-sm text-black rounded-lg px-3 py-1 hover:bg-gray-200')

            with ui.row().classes('w-full p-2 bg-gray-100 rounded-lg justify-between items-center'):
                ui.label("Invoice #123455").classes('font-medium')
                ui.label("₵49.00").classes('font-bold text-green-600')
                ui.label("2024-08-20").classes('text-sm text-gray-500')
                ui.button("View Invoice").classes('text-sm text-black rounded-lg px-3 py-1 hover:bg-gray-200')
