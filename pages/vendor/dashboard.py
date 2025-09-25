from nicegui import ui
from components.sidebar import show_sidebar


@ui.page("/vendor/dashboard")
def vendor_dashboard():
    show_sidebar()

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

        # Summary cards
        with ui.row().classes('w-full gap-6'):
            for label, value in [
                ('Total Adverts', '12'),
                ('Categories', '5'),
                ('Total Views', '2,340'),
            ]:
                with ui.card().classes('w-1/3 p-4'):
                    ui.label(label).classes('text-lg text-gray-600')
                    ui.label(value).classes('text-3xl font-bold')

        # Analytics
        ui.label('Analytics').classes('text-2xl font-bold text-gray-800')

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
                    'data': [
                        {'value': 6, 'name': 'Electronics'},
                        {'value': 4, 'name': 'Fashion'},
                        {'value': 2, 'name': 'Furniture'},
                    ],
                    'emphasis': {
                        'itemStyle': {
                            'shadowBlur': 10,
                            'shadowOffsetX': 0,
                            'shadowColor': 'rgba(0, 0, 0, 0.5)',
                        }
                    },
                }],
            }).style('width:100%; height:100%;')

        with ui.card().classes('w-full h-96 p-4'):
            ui.echart({
                'title': {'text': 'Views per Advert', 'left': 'center'},
                'tooltip': {'trigger': 'axis'},
                'xAxis': {'type': 'category', 'data': ['Advert 1', 'Advert 2', 'Advert 3']},
                'yAxis': {'type': 'value'},
                'series': [{
                    'data': [450, 310, 120],
                    'type': 'bar',
                    'barWidth': '50%',
                    'itemStyle': {'color': '#1f2937'},
                }],
            }).style('width:100%; height:100%;')

        # Adverts list
        ui.label('My Adverts').classes('text-2xl font-bold text-gray-800')

        with ui.row().classes('w-full gap-6 flex-wrap'):

            def advert_card(title, category, views, advert_id):
                with ui.card().classes('w-72 p-4'):
                    ui.image('https://via.placeholder.com/300x150').classes('w-full h-32 rounded mb-4')
                    ui.label(title).classes('text-lg font-semibold text-gray-800')
                    ui.label(f'Category: {category}').classes('text-sm text-gray-600')
                    ui.label(f'Views: {views}').classes('text-sm text-gray-600 mb-2')
                    with ui.row().classes('justify-between'):
                        ui.button('Edit',on_click=lambda: ui.navigate.to(f"/vendor/edit_event?advert_id={id}")).classes('bg-black text-white px-3 py-1 rounded hover:bg-gray-800')
                        ui.button('Delete').classes('bg-black text-white px-3 py-1 rounded hover:bg-gray-800')

            # Example adverts
            advert_card('Advert 1', 'Electronics', 450, advert_id=1)
            advert_card('Advert 2', 'Fashion', 310, advert_id=2)
            advert_card('Advert 3', 'Furniture', 120, advert_id=3)