from nicegui import ui

def show_header():
    with ui.row():
        ui.link("Home","/")
        ui.link("Add event","/add_event")
        ui.link("edit event","edit_event")
        ui.link("view event","/view_event")
      
