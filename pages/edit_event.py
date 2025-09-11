from nicegui import ui 

def show_edit_event_page():
    with ui.column().classes(
        "max-w-2xl mx-auto mt-24 p-8 rounded-2xl shadow-2xl bg-white space-y-6 bg-[#e3d5ca]" 
    ):
        # Title
        ui.label('EDIT YOUR ADVERT HERE').classes(
            'font-extrabold text-4xl tracking-wide text-center text-gray-800'
        )

        # Title input
        ui.input('Title').props('outlined').classes(
            'w-full rounded-lg border-gray-300 focus:ring-2 focus:ring-indigo-500'
        )

        
        ui.textarea('Item Description').props('outlined').classes(
            'w-full rounded-lg border-gray-300 focus:ring-2 focus:ring-indigo-500'
        )

        # Price
        ui.number('Price').props('outlined').classes(
            'w-full rounded-lg border-gray-300 focus:ring-2 focus:ring-indigo-500'
        )

        # Categories
        ui.label('Categories').classes('font-medium text-gray-700')
        ui.select(
            ['CLOTHINGS', 'TUMBLERS', 'CARS', 'FURNITURE']
        ).classes("w-full rounded-lg").props('outlined')

        # Upload
        ui.label('Upload image').classes('font-medium text-gray-700')
        ui.upload(
            on_upload=lambda e: ui.notify(f'Uploaded'),
            on_rejected=lambda: ui.notify('Rejected!'),
            max_file_size=5_000_000
        ).classes('w-full rounded-lg border border-dashed border-gray-400 p-4')

        # Submit button
        def submit():
            ui.notify(f'Add Submitted Successfully')

        ui.button('Submit', on_click=submit).classes(
            'mt-6 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 px-6 rounded-xl shadow-md w-full'
        )
        def delete():
            ui.notify(f'Deleted Successfully')
        ui.button('Delete', on_click=delete).classes(
            'mt-6 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 px-6 rounded-xl shadow-md w-full'
        )