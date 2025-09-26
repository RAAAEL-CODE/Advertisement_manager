from nicegui import ui


@ui.page("/")  # ✅ This will now be your first page
def landing_page():
    # Apply background image to the whole page
    ui.query("body").style(
        """
        background-image: url("Assets/Blue Modern Landing Page Youtube Thumbnail .png");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center center;
        """
    )

    with ui.column().classes(
        "h-screen w-full items-center justify-center text-white bg-black/20"
    ):  # added semi-transparent overlay for readability
        ui.label("Welcome to RAAEL ADS").classes("text-5xl font-bold mb-6")
        ui.label("Buy and sell cars, furniture, clothes, tumblers and more.").classes(
            "text-xl mb-8"
        )

        with ui.row().classes("gap-4"):
            # Sign In Button with loading effect
            signin_btn = ui.button(
                "Sign In",
                on_click=lambda e: start_loading(signin_btn, "/signin"),
            ).classes(
                "bg-black text-white font-bold px-6 py-3 rounded-xl shadow-lg hover:bg-black"
            )

            # Sign Up Button with loading effect
            signup_btn = ui.button(
                "Sign Up",
                on_click=lambda e: start_loading(signup_btn, "/signup"),
            ).classes(
                "bg-black text-white font-bold px-6 py-3 rounded-xl shadow-lg hover:bg-black"
            )

    # Function to handle loading effect before navigating
    def start_loading(button, route: str):
        button.props("loading")  # show loading spinner
        ui.timer(
            1, lambda: ui.navigate.to(route), once=True
        )  # delay 1 sec then navigate
