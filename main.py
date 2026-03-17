import customtkinter as ctk
import sys
import os

# ---------------------------------------------------------
#  Recipe Encyclopedia - Starter Application
#  Opens directly to a Welcome Screen
# ---------------------------------------------------------

# -----
# recipe display frame:
# -----
class RecipeDisplay(ctk.CTkFrame):
    def __init__(self, master, recipe_name):
        super().__init__(master)

        # recipe title:
        self.title_label = ctk.CTkLabel(
            self,
            text=recipe_name,
            font=("Segoe UI", 28, "bold")
        )
        self.title_label.pack(pady=(40, 20))

        # recipe details placeholder:
        self.info_label = ctk.CTkLabel(
            self,
            text="The full recipe details and instructions will be displayed here.",
            font=("Segoe UI", 16)
        )
        self.info_label.pack(pady=10)

# -----

class WelcomeScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Title
        self.title_label = ctk.CTkLabel(
            self,
            text="Recipe Encyclopedia",
            font=("Segoe UI", 32, "bold")
        )
        self.title_label.pack(pady=(80, 10))

        # Subtitle
        self.subtitle_label = ctk.CTkLabel(
            self,
            text="Your journey into organized cooking starts here.",
            font=("Segoe UI", 16)
        )
        self.subtitle_label.pack(pady=(0, 20))

        # -----
        # app usage instructions:
        # -----
        self.usage_label = ctk.CTkLabel(
            self,
            text="To begin, simply select a recipe from the sidebar on the left.\n"
                 "The details will appear here automatically.",
            font=("Segoe UI", 14),
            justify="center"
        )
        self.usage_label.pack(pady=20)

        # Footer
        self.footer_label = ctk.CTkLabel(
            self,
            text="Â© 2026 Recipe Encyclopedia Project",
            font=("Segoe UI", 12)
        )
        self.footer_label.pack(side="bottom", pady=20)


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Recipe Encyclopedia")
        self.geometry("900x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # -----
        # layout configuration:
        # -----
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # sidebar setup:
        self.sidebar_frame = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")

        # sidebar label:
        self.sidebar_label = ctk.CTkLabel(
            self.sidebar_frame,
            text="Recipes",
            font=("Segoe UI", 20, "bold")
        )
        self.sidebar_label.pack(pady=20, padx=20)

        # sidebar placeholder buttons:
        self.recipe_one = ctk.CTkButton(
            self.sidebar_frame,
            text="Classic Beef Stew",
            command=lambda: self.show_recipe("Classic Beef Stew")
        )
        self.recipe_one.pack(pady=10, padx=20)

        self.recipe_two = ctk.CTkButton(
            self.sidebar_frame,
            text="Homemade Pasta",
            command=lambda: self.show_recipe("Homemade Pasta")
        )
        self.recipe_two.pack(pady=10, padx=20)

        # content container setup:
        self.container = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.container.grid(row=0, column=1, sticky="nsew")

        # default to welcome screen:
        self.current_frame = None
        self.show_welcome_screen()

    def clear_frame(self):
        if self.current_frame is not None:
            self.current_frame.destroy()

    # -----
    # frame navigation logic:
    # -----
    def show_welcome_screen(self):
        self.clear_frame()
        self.current_frame = WelcomeScreen(self.container)
        self.current_frame.pack(fill="both", expand=True)

    def show_recipe(self, name):
        self.clear_frame()
        self.current_frame = RecipeDisplay(self.container, name)
        self.current_frame.pack(fill="both", expand=True)
    # -----


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
    
