from operations import ContrastOperation, BrightnessOperation, GrayscaleOperation, PaddingOperation, ThresholdOperation, BlendingOperation

class Router:
    """
    Maps user choices to corresponding controller methods or operations.
    """
    def __init__(self, controller):
        self.controller = controller
        self.routes = {
            '1': lambda: controller.transform_image(BrightnessOperation),
            '2': lambda: controller.transform_image(ContrastOperation),
            '3': lambda: controller.transform_image(GrayscaleOperation),
            '4': lambda: controller.transform_image(PaddingOperation),
            '5': lambda: controller.transform_image(ThresholdOperation),
            '6': lambda: controller.transform_image(BlendingOperation),
            '7': controller.undo_last_operation,
            '8': controller.history_of_operations,
            '9': controller.exit_application
        }

    def execute(self, choice):
        """
        Executes the method mapped to the user's choice.

        Args:
            choice (str): The user's menu choice.

        Raises:
            KeyError: If the choice is not mapped.
        """
        if choice in self.routes:
            self.routes[choice]()
        else:
            print("Invalid choice. Try again.")