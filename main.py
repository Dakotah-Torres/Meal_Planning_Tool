
from nicegui import ui
from app.views.add_ingredient import app




def main():
    
    app()
    ui.run(native=True, window_size=(1000, 700), fullscreen=False)


main()
