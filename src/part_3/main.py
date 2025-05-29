from ExitApplication import ExitApplication
from Router import Router
from Controler import Controller
from Presentation import Presentation

def main():
    """
    Entry point of the modular photo editing application.
    """
    try:
        presentation = Presentation()
        image = presentation.get_initial_image()

        controller = Controller(image)
        router = Router(controller)

        while True:
            choice = presentation.show_menu()
            try:
                router.execute(choice)
            except ExitApplication:
                print("Exiting application.")
                break
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()