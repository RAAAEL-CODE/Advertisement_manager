from nicegui import ui, events, run, app
import requests
from utils.api import base_url
from components.sidebar import show_sidebar

flyer_content = None
_create_event_btn: ui.button = None


def _run_create_event(data, files, token):
    return requests.post(
        f"{base_url}/adverts/",
        data=data,
        files=files,
        headers={"Authorization": f"Bearer {token}"},
    )


async def add_event(data, files):

    response = await run.cpu_bound(
        _run_create_event, data, files, app.storage.user.get("access_token")
    )
    print(response.json())


def handle_flyer_upload(e: events.UploadEventArguments):
    global flyer_content
    flyer_content = ("flyer.jpg", e.content.read(), "image/jpeg")
    ui.notify("File uploaded successfully")


@ui.page("/vendor/add_event")
def show_add_event_page():
    global _create_event_btn
    # Correct: Call show_sidebar() once and at the top level of the page function.
    show_sidebar()

    with ui.column().classes(
        "w-full max-w-2xl mx-auto mt-24 p-8 rounded-2xl shadow-2xl bg-white space-y-6"
    ):

        ui.label("CREATE A NEW ADVERT").classes(
            "font-extrabold text-4xl tracking-wide text-center text-gray-800"
        )

        title = ui.input("Title").props("outlined").classes("w-full")
        description = (
            ui.textarea("Item Description").props("outlined").classes("w-full")
        )
        price = ui.number("Price").props("outlined").classes("w-full")

        ui.label("Categories").classes("font-medium text-gray-700")
        categories = (
            ui.select(["Clothing", "Tumblers", "Cars", "Furniture", "Bags"])
            .props("outlined")
            .classes("w-full")
        )

        ui.label("Upload image").classes("font-medium text-gray-700")
        flyer = (
            ui.upload(on_upload=handle_flyer_upload)
            .classes("w-full rounded-lg border border-dashed border-gray-400 p-4")
            .props("color=black")
        )

        async def submit():
            global flyer_content
            ad_data = {
                "title": title.value,
                "description": description.value,
                "price": price.value,
                "category": categories.value,
            }
            _create_event_btn.props(add="disable loading")
            response = await run.cpu_bound(
                _run_create_event,
                ad_data,
                {"flyer": flyer_content},
                app.storage.user.get("access_token"),
            )
            print(response.status_code, response.content)
            _create_event_btn.props(remove="disable loading")
            if response.status_code == 200:
                ui.notify("Ad submitted successfully!")
            else:
                ui.notify(f"Failed: {response.text}")

        _create_event_btn = (
            ui.button("Submit", on_click=submit)
            .classes(
                "mt-6 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 px-6 rounded-xl shadow-md w-full"
            )
            .props("color=black")
        )

        def delete():
            ui.notify("Deleted Successfully")

        ui.button("Delete", on_click=delete).classes(
            "mt-3 bg-red-600 hover:bg-red-700 text-white font-semibold py-3 px-6 rounded-xl shadow-md w-full"
        ).props("color=black")
