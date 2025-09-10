from nicegui import ui

def show_welcome_page():
   with ui.row().classes("w-screen h-screen relative"):
    ui.video("Assets/Pink Retro Welcome to my Channel Youtube Video.mp4", autoplay=True,
             loop=True,
               muted=True,
               controls=False).classes("absolute insert-0 w-full h-full object-cover z-0")


