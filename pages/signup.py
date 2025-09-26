from nicegui import ui, run
import requests
from utils.api import base_url


current_image_index = 0
_signup_btn: ui.button = None


def _run_signup(data):
    return requests.post(f"{base_url}/users/register", data=data)


async def _signup(data):
    _signup_btn.props(add="disable loading")
    response = await run.cpu_bound(_run_signup, data)
    print(response.status_code, response.content)
    _signup_btn.props(remove="disable loading")
    if response.status_code == 200:
        return ui.navigate.to("/signin")
    elif response.status_code == 409:
        return ui.notify(message="User already exists!", type="warning")


@ui.page("/signup")
def show_signup_page():

    with ui.column().classes("col-span-1 items-center justify-center w-[1/2]"):

        global current_image_index
        background_images = [
            "Assets/pexels-fotoaibe-1743227.jpg",
            "Assets/_Beige and Brown Fashion Trends (Poster (Landscape)).png",
            "Assets/Black  and White Modern Car Sale Facebook Post.png",
        ]

        ui.query("body").style(
            f'background-image: url("{background_images[current_image_index]}");'
            "background-size: cover;"
            "background-repeat: no-repeat;"
            "background-attachment: fixed;"
            "background-position: center center;"
        )

        def change_background():
            global current_image_index
            current_image_index = (current_image_index + 1) % len(background_images)
            ui.query("body").style(
                f'background-image: url("{background_images[current_image_index]}");'
            )

        ui.timer(5, change_background)

    with ui.column().classes("min-h-screen w-full items-center justify-center"):
        with ui.card().classes("w-full max-w-xl p-8 shadow-lg rounded-xl"):
            ui.label("Sign Up with").classes(
                "text-4xl font-bold mb-6 items-center self-center"
            )
            ui.label("RAAEL ADS").classes(
                "text-4xl font-bold items-center text-blue self-center"
            )

            ui.label("Choose your role:").classes("text-lg mb-4 font-semibold")

            role = {"value": None}  # store selected role

            with ui.row().classes("gap-8 items-center justify-center mb-6 ml-20"):
                # Consumer card
                with ui.card().classes(
                    "cursor-pointer w-20 items-center p-4 hover:shadow-lg"
                ).props("flat bordered") as consumer_card:
                    ui.icon("person", size="20px", color="green").classes(
                        "p-4 rounded-full bg-green-100"
                    )
                    ui.label("Consumer").classes("font-bold")
                    consumer_card.on("click", lambda _: select_role("Consumer"))

                # Vendor card
                with ui.card().classes(
                    "cursor-pointer w-20 items-center p-4 hover:shadow-lg"
                ).props("flat bordered") as vendor_card:
                    ui.icon("store", size="20px", color="blue").classes(
                        "p-4 rounded-full bg-blue-100"
                    )
                    ui.label("Vendor").classes("font-bold")
                    vendor_card.on("click", lambda _: select_role("Vendor"))

            form_container = ui.column().classes("space-y-4 w-full")

            ui.label("Already have an account?").classes(
                "text-sm text-gray-600 text-center items-center"
            )
            ui.link("Sign in", "/signin").classes(
                "text-sm text-black font-bold hover:underline text-center items-center"
            )

            def select_role(selected):
                role["value"] = selected
                render_form()

            def render_form():
                form_container.clear()
                if role["value"] == "Consumer":
                    with form_container:
                        name = ui.input("User Name").classes("w-full").props("outlined")
                        email = (
                            ui.input("Email")
                            .props("type=email outlined")
                            .classes("w-full")
                        )
                        password = (
                            ui.input(
                                placeholder="Password",
                                password=True,
                                password_toggle_button=True,
                            )
                            .props("type=password outlined")
                            .classes("w-full")
                        )
                        global _signup_btn
                        _signup_btn = ui.button(
                            "Sign Up",
                            on_click=lambda: _signup(
                                {
                                    "username": name.value,
                                    "email": email.value,
                                    "password": password.value,
                                    "role": "Consumer",
                                }
                            ),
                        ).classes("w-full bg-black")
                elif role["value"] == "Vendor":
                    with form_container:
                        name = (
                            ui.input(placeholder="Business Name")
                            .classes("w-full")
                            .props("outlined")
                        )
                        email = (
                            ui.input(placeholder="Email")
                            .props("type=email outlined")
                            .classes("w-full")
                        )
                        location = (
                            ui.input(placeholder="Business Location")
                            .props("outlined")
                            .classes("w-full")
                        )
                        password = (
                            ui.input(
                                placeholder="Password",
                                password=True,
                                password_toggle_button=True,
                            )
                            .props("type=password outlined")
                            .classes("w-full")
                        )
                        _signup_btn = ui.button(
                            "Sign Up",
                            on_click=lambda: _signup(
                                {
                                    "username": name.value,
                                    "email": email.value,
                                    "location": location.value,
                                    "password": password.value,
                                    "role": "Vendor",
                                }
                            ),
                        ).classes("w-full bg-black")

            render_form()
