# from nicegui import ui, app


# def show_header():
#     with ui.row().classes(
#         "fixed top-0 left-0 w-full justify-between items-center px-8 py-4 bg-black text-white shadow-md z-50"
#     ):
#         # Logo / App name
#         ui.image("Assets/Black & White Minimalist Business Logo.jpeg").classes(
#             "w-[100px] h-[70]"
#         )

#         # Navigation links (spread across)
#         with ui.row().classes("flex-1 justify-evenly"):
#             ui.link("Home", "/").classes("no-underline text-white hover:text-gray-300")
#             ui.link("Create Advert", "/vendor/add_event").classes(
#                 "no-underline text-white hover:text-gray-300"
#             )
#             if app.storage.user.get("access_token"):
#                 ui.button("Signout")
#             else:
#                 ui.link("signin", "/signin").classes(
#                     "no-underline text-white hover:text-gray-300"
#                 )
#                 ui.link("", "/view_event").classes(
#                     "no-underline text-white hover:text-gray-300"
#                 )
#                 ui.link("signup", "/signup").classes(
#                     "no-underline text-white hover:text-gray-300"
#                 )
from nicegui import ui, app


def show_header():
    # Define the signout logic
    def signout_user():
        # Clear all user-related data from the storage
        app.storage.user.clear()
        # Redirect the user to the home page
        ui.navigate.to('/')

    with ui.row().classes(
        "fixed top-0 left-0 w-full justify-between items-center px-8 py-4 bg-black text-white shadow-md z-50"
    ):
        # Logo / App name
        ui.image("Assets/Black & White Minimalist Business Logo.jpeg").classes(
            "w-[100px] h-[70]"
        )

        # Navigation links (spread across)
        with ui.row().classes("flex-1 justify-evenly"):
            ui.link("Home", "/").classes("no-underline text-white hover:text-gray-300")
            ui.link("Create Advert", "/vendor/add_event").classes(
                "no-underline text-white hover:text-gray-300"
            )
            
            if app.storage.user.get("access_token"):
                # Make the button functional and style it to match the links
                ui.button("Signout", on_click=signout_user).props('flat').classes("no-underline text-white hover:text-gray-300")
            else:
                ui.link("signin", "/signin").classes(
                    "no-underline text-white hover:text-gray-300"
                )
                ui.link("", "/view_event").classes(
                    "no-underline text-white hover:text-gray-300"
                )
                ui.link("signup", "/signup").classes(
                    "no-underline text-white hover:text-gray-300"
                )
