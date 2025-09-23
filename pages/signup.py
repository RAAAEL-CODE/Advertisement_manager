from nicegui import ui

current_image_index = 0

@ui.page("/signup")
def show_signup_page():
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

    with ui.column().classes(
        "min-h-screen w-full items-center justify-center"
    ):
        with ui.card().classes("w-full max-w-xl p-8  shadow-lg rounded-xl"):
            ui.label("Sign Up with").classes("text-4xl font-bold mb-6 items-center self-center")
            ui.label('RAAEL ADS').classes("text-4xl font-bold items-center text-blue self-center")

            # Select button (dropdown)
            register = ui.radio(["Consumer", "Vendor"], value="Consumer").classes(
                "w-full flex flex-row"
            )

            form_container = ui.column().classes("space-y-4 w-full")
            ui.label("Already have an account?").classes(
                "text-sm text-gray-600 text-center"
            )
            ui.link("Sign in", "/signin").classes(
                "text-sm text-black font-bold hover:underline text-center"
            )

            def render_form():
                form_container.clear()
                if register.value == "Consumer":
                    with form_container:
                        name = ui.input("User Name").classes("w-full").props('outlined')
                        email = ui.input("Email").props("type=email outlined").classes("w-full")
                        password = (
                            ui.input(
                                placeholder="Password",
                                password=True,
                                password_toggle_button=True,
                            )
                            .props("type=password outlined")
                            .classes("w-full")
                        )
                        confirm_password = (
                            ui.input(
                                placeholder="Confirm Password",
                                password=True,
                                password_toggle_button=True,
                            )
                            .props("type=password outlined")
                            .classes("w-full")
                        )
                        ui.button(
                            "Sign Up",
                            on_click=lambda: ui.notify("User Registered!"),
                        ).classes("w-full")
                else:
                    with form_container:
                        name = ui.input(placeholder="Business Name").classes("w-full").props('outlined')
                        email = (
                            ui.input(placeholder="Email")
                            .props("type=email outlined")
                            .classes("w-full")
                        )
                        Location= (
                            ui.input(placeholder="Business Location")
                            .props("type=location outlined")
                            .classes("w-full"))
                        password = (
                            ui.input(
                                placeholder="Password",
                                password=True,
                                password_toggle_button=True,
                            )
                            .props("type=password outlined")
                            .classes("w-full")
                        )
                        confirm_password = ui.input(
                            placeholder="Confirm Password",
                            password=True,
                            password_toggle_button=True,
                        ).classes("w-full").props('outlined')

                        ui.button(
                            "Sign Up",
                            on_click=lambda: ui.notify(
                                "Vendor Registered!", ui.navigate.to(f"/signin")
                            ),
                        ).classes("w-full")

            render_form()

            register.on_value_change(lambda e: render_form())