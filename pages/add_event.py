from nicegui import ui 

def show_add_event_page():
    with ui.column().classes(
        'max-w-2xl mx-auto mt-24 p-8 rounded-2xl shadow-2xl bg-white space-y-6'
    ):
        # Title
        ui.label('CREATE A NEW ADVERT').classes(
            'font-extrabold text-4xl tracking-wide text-center text-gray-800'
        )

        # Inputs
        title = ui.input('Title').props('outlined').classes(
            'w-full rounded-lg border-gray-300 focus:ring-2 focus:ring-indigo-500'
        )

        description = ui.textarea('Item Description').props('outlined').classes(
            'w-full rounded-lg border-gray-300 focus:ring-2 focus:ring-indigo-500'
        )

        price = ui.number('Price').props('outlined').classes(
            'w-full rounded-lg border-gray-300 focus:ring-2 focus:ring-indigo-500'
        )

        # Categories
        ui.label('Categories').classes('font-medium text-gray-700')
        categories = ui.select(
            ['CLOTHINGS', 'TUMBLERS', 'CARS', 'FURNITURE']
        ).classes("w-full rounded-lg").props('outlined')

        # Upload
        ui.label('Upload image').classes('font-medium text-gray-700')
        flyer = ui.upload(
            on_upload=lambda e: ui.notify('Uploaded'),
            on_rejected=lambda: ui.notify('Rejected!'),
            max_file_size=5_000_000
        ).classes('w-full rounded-lg border border-dashed border-gray-400 p-4')

        # Submit button
        def submit():
            ad_data={
                'title':title.value,
                'description':description.value,
                'price':price.value,
                'category':categories.value,

            }
            print(ad_data)
            ui.notify(
                f"Ad Submitted: {title.value}, {description.value}, {price.value}, {categories.value}"
            )

        ui.button('Submit', on_click=submit).classes(
            'mt-6 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 px-6 rounded-xl shadow-md w-full'
        )

        # Delete button
        def delete():
            ui.notify('Deleted Successfully')

        ui.button('Delete', on_click=delete).classes(
            'mt-3 bg-red-600 hover:bg-red-700 text-white font-semibold py-3 px-6 rounded-xl shadow-md w-full'
        )


