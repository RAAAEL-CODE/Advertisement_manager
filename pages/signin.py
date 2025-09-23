from nicegui import ui

# The global variable should be defined outside of any function
current_image_index = 0

@ui.page("/signin")
def show_signin_page():
    with ui.grid().classes('grid-cols-2 h-screen w-[1/2]'):
        with ui.column().classes('col-span-1 items-center justify-center w-[1/2]'):

            global current_image_index
            background_images = [
                'Assets/pexels-fotoaibe-1743227.jpg',
                'Assets/_Beige and Brown Fashion Trends (Poster (Landscape)).png',
                'Assets/Black  and White Modern Car Sale Facebook Post.png'
            ]

            # Initialize the background image and timer.
            ui.query("body").style(
                f'background-image: url("{background_images[current_image_index]}");'
                'background-size: cover;'
                'background-repeat: no-repeat;'
                'background-attachment: fixed;'
                'background-position: center center;')
            
            def change_background():
                global current_image_index
                current_image_index = (current_image_index + 1) % len(background_images)
                ui.query("body").style(f'background-image: url("{background_images[current_image_index]}");')
            
            ui.timer(5, change_background)


        with ui.column().classes('items-center justify-center self-center'):
           

            with ui.card().classes('text-white p-6 rounded-lg bg-white bg-opacity-70 backdrop-blur-md w-[600px] mr-60  items-center self-center absolute-center'):
                ui.label('Sign in to ').classes('text-4xl font-bold text-black')
                ui.label('RAAEL ADS').classes('text-4xl font-bold text-blue')
                email = ui.input(label='Email').props("outlined").classes('w-full')
                password = ui.input(label='Enter password', password=True, password_toggle_button=True).props('outlined').classes("w-full")
                with ui.row().classes('justify-between w-full mt-4 items-center'):
                    ui.button('Sign in').classes("w-[100px] rounded")
                    ui.link('forgot password', target="#").classes('text-xs text-blue-300 hover:text-blue-500')