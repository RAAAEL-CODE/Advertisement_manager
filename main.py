from nicegui import ui,app
from components.header import show_header
from pages.home import show_home_page
from pages.view_event import show_view_page
from pages.welcome import show_welcome_page
from pages.vendor.dashboard import*
from pages.vendor.add_event import *
from pages.vendor.edit_event import *
from pages.vendor.events import *
from pages.signin import *
from pages.signup import *


app.add_static_files("/Assets", "Assets")


@ui.page("/")
def home_page():
    show_header()
    show_welcome_page()
    show_home_page()
    
                                                            
@ui.page("/view_event")
def view_event_page(id=""):
    show_header()
    show_view_page(id)


ui.run(tailwind="[bg-e3d5ca]")

