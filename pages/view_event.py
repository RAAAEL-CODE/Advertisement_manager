from nicegui import ui, run, app
import requests
from utils.api import base_url


#
@ui.page("/view_event/{id}")
def show_view_page(id: str):  # keep str for safety
    print("Fetching advert:", f"{base_url}/adverts/{id}")  # debug log

    # Fetch single advert
    response = requests.get(f"{base_url}/adverts/{id}")
    #
    if response.status_code != 200:
        ui.notify(f"Could not load advert: {response.status_code}", type="negative")
        ui.navigate.to("/")
        return

    advert = response.json()["data"]

    # === Advert Details Card ===
    with ui.card().classes(
        "w-[40rem] h-1/2 sm:w-[50%] md:w-[30%] lg:w-[60%] mx-auto p-6 bg-white rounded-xl shadow-lg mt-24"
    ):
        ui.image(advert["flyer"]).classes(
            "w-3/3 h-full rounded-lg mb-4 shadow-xl transition-transform duration-300 hover:scale-110"
        )
        ui.label(advert["title"]).classes("text-xl font-semibold")
        ui.label(f"Price: GHC {advert['price']}").classes(
            "text-gray-700 text-xl shadow-xl"
        )
        ui.label(f"Category: {advert['category']}").classes("text-xl")
        ui.label(f"Description: {advert['description']}").classes(
            "text-gray-600 text-xl"
        )

        with ui.grid(columns=3).classes(
            "items-center justify-center self-center gap-4 mt-6"
        ):
            ui.button("Exit", on_click=lambda: ui.navigate.to("/")).classes(
                "bg-black w-[150px] text-white px-4 py-2 rounded-lg self-center"
            )
            ui.button(
                "Add to Cart",
                on_click=lambda: ui.notify(f"{advert['title']} added to cart!"),
            ).classes(
                "bg-black w-[150px] text-white  text-bold px-4 py-2 rounded-lg self-center"
            )
            ui.button(
                "Buy Now",
                on_click=lambda: ui.notify(f"Proceeding to buy {advert['title']}"),
            ).classes(
                "bg-black w-[150px] text-white text-bold px-4 py-2 rounded-lg self-center"
            )

    # === Related Items Section ===
    ui.label("Related Items").classes("text-2xl font-bold mt-12 text-center")

    related_response = requests.get(f"{base_url}/adverts")
    if related_response.status_code == 200:
        all_adverts = related_response.json().get("data", [])
        # filter adverts with the same category but exclude the current one
        related_adverts = [
            a
            for a in all_adverts
            if a["category"] == advert["category"] and str(a["id"]) != str(id)
        ]

        if related_adverts:
            with ui.grid(columns=3).classes("gap-6 p-6"):
                for item in related_adverts[:4]:
                    with ui.card().classes(
                        "p-4 rounded-xl shadow-md hover:shadow-xl transition cursor-pointer w-[300px] h-[350px]"
                    ).on(
                        "click",
                        lambda e, a=item: ui.navigate.to(f"/view_event/{a['id']}"),
                    ):
                        ui.image(item["flyer"]).classes(
                            "h-40 w-full object-cover rounded-lg mb-2"
                        )
                        ui.label(item["title"]).classes("font-semibold")
                        ui.label(f"GHC {item['price']}").classes("text-gray-700")
        else:
            ui.label("No related items found.").classes(
                "text-gray-500 text-center mt-4"
            )
    else:
        ui.label("Could not fetch related items.").classes(
            "text-red-500 text-center mt-4"
        )
