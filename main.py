from nicegui import ui, app
from pages.landing_page import *

from components.header import show_header
from pages.home import show_home_page
from pages.view_event import show_view_page
from pages.welcome import show_welcome_page
from pages.vendor.dashboard import *
from pages.vendor.add_event import *
from pages.vendor.edit_event import *
from pages.vendor.events import *
from pages.vendor.billing import *
from pages.vendor.support import *
from pages.signin import *
from pages.signup import *

# serve static assets (images, flyers, etc.)
app.add_static_files("/Assets", "Assets")


@ui.page("/home")
def home_page():
    show_header()
    show_welcome_page()
    show_home_page()


@ui.page("/view_event/{id}")  # <-- fix: must accept {id}, not plain /view_event
def view_event_page(id: str):
    show_header()
    show_view_page(id)


ui.run(storage_secret="Raael advertisement website created, vetted and approved by FDA")
