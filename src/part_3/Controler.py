import os
import cv2
import matplotlib.pyplot as plt
from ExitApplication import ExitApplication

class Controller:
    def __init__(self, image):
        self.img_versions = [image.copy()]
        self.actions = []

    def transform_image(self, operationConstructor):
        """
        Apply an operation to the latest image, update history, and display the new image.

        Uses matplotlib to show side-by-side: [original | preview].
        """
        while True:
            try:
                operation = operationConstructor(self.img_versions[-1])
                new_image = operation.transformed_img()
                action_desc = operation.action_desc()
                self.img_versions.append(new_image.copy())
                self.actions.append(action_desc)
                print(f"Operation done: {action_desc}")

                fig, axes = plt.subplots(1, 2, figsize=(10, 5))
                fig.suptitle(f"Operation: {action_desc}", fontsize=14)

                original_img = self.img_versions[-2] if len(self.img_versions) >= 2 else self.img_versions[-1]
                original_img_rgb = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB) if len(original_img.shape) == 3 else original_img
                axes[0].imshow(original_img_rgb, cmap='gray' if len(original_img.shape) == 2 else None)
                axes[0].set_title("Original")
                axes[0].axis('off')

                preview_img_rgb = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB) if len(new_image.shape) == 3 else new_image
                axes[1].imshow(preview_img_rgb, cmap='gray' if len(new_image.shape) == 2 else None)
                axes[1].set_title("Preview")
                axes[1].axis('off')

                plt.tight_layout()
                plt.show()
                break
            except Exception as e:
                print(f"Error applying operation: {e}")

    def undo_last_operation(self):
        if len(self.img_versions) > 1:
            self.img_versions.pop()
            self.actions.pop()
            print("Undone last operation.")
        else:
            print("No previous state to revert to.")

    def history_of_operations(self):
        print("==== History of Operations ====")
        if self.actions:
            for i, act in enumerate(self.actions, 1):
                print(f"{i}. {act}")
        else:
            print("No actions performed yet.")

    def exit_application(self):
        save_choice = input("Save the final image? (y/n): ").strip().lower()
        if save_choice == 'y':
            save_name = input("Enter filename to save (with extension, e.g., output.jpg): ").strip()
            script_dir = os.path.dirname(os.path.abspath(__file__))
            save_path = os.path.abspath(os.path.join(script_dir, f'../../img/part_3/{save_name}'))
            cv2.imwrite(save_path, self.img_versions[-1])
            print(f"Final image saved as {save_path}")
        raise ExitApplication()