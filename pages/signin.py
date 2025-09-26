from nicegui import ui, run, app
import requests
from utils.api import base_url

_login_btn: ui.button = None


def _run_login(data):
    return requests.post(f"{base_url}/users/login", data=data)


def _get_user_profile(token: str):
    headers = {"Authorization": f"Bearer {token}"}
    return requests.get(f"{base_url}/users/register", headers=headers)


async def _login(data):
    _login_btn.props(add="disable loading")
    response = await run.cpu_bound(_run_login, data)
    print(response.status_code, response.content)
    _login_btn.props(remove="disable loading")

    if response.status_code == 200:
        json_data = response.json()
        access_token = json_data.get("access_token")
        if not access_token:
            ui.notify("No access token returned!", type="negative")
            return

        app.storage.user["access_token"] = access_token

        # ✅ Fetch user profile
        profile_response = await run.cpu_bound(_get_user_profile, access_token)
        if profile_response.status_code == 200:
            profile = profile_response.json()
            print("User profile:", profile)  # Debugging output

            # Use "role" instead of "user_type"
            role = profile.get("role", "Consumer")

            if role == "Vendor":
                ui.navigate.to("/dashboard")
            else:
                ui.navigate.to("/home")
        else:
            ui.notify("", type="warning")
            ui.navigate.to("/home")  # fallback
    else:
        ui.notify("Login failed! Please check your email or password.", type="negative")


# The global variable should be defined outside of any function
current_image_index = 0


@ui.page("/signin")
def show_signin_page():
    global _login_btn
    with ui.grid().classes("grid-cols-2 h-screen w-[1/2]"):
        with ui.column().classes("col-span-1 items-center justify-center w-[1/2]"):

            global current_image_index
            background_images = [
                "Assets/pexels-fotoaibe-1743227.jpg",
                "Assets/_Beige and Brown Fashion Trends (Poster (Landscape)).png",
                "Assets/Black  and White Modern Car Sale Facebook Post.png",
            ]

            # Initialize the background image and timer
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

        with ui.column().classes("items-center justify-center self-center"):
            with ui.card().classes(
                "text-white p-6 rounded-lg bg-white bg-opacity-70 backdrop-blur-md "
                "w-[600px] mr-60 items-center self-center absolute-center"
            ):
                ui.label("Sign in to ").classes("text-4xl font-bold text-black")
                ui.label("RAAEL ADS").classes("text-4xl font-bold text-blue")

                email = ui.input(label="Email").props("outlined").classes("w-full")
                password = (
                    ui.input(
                        label="Enter password",
                        password=True,
                        password_toggle_button=True,
                    )
                    .props("outlined")
                    .classes("w-full")
                )

                with ui.row().classes("justify-between w-full mt-4 items-center"):
                    _login_btn = (
                        ui.button(
                            "Sign in",
                            on_click=lambda: _login(
                                {"email": email.value, "password": password.value}
                            ),
                        )
                        .classes("w-[100px] rounded bg-black text-white text-bold")
                        .props("flat dense no-caps")
                    )

                    ui.link("forgot password", target="#").classes(
                        "text-xs text-blue-300 hover:text-blue-500"
                    )
