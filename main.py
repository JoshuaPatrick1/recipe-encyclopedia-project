import customtkinter as ctk
import sys
import os

# ---------------------------------------------------------
#  Recipe Encyclopedia - Starter Application
#  Opens directly to a Welcome Screen
# ---------------------------------------------------------

class WelcomeScreen(ctk.CTkFrame):
    def __init__(self, master, switch_callback):
        super().__init__(master)

        self.switch_callback = switch_callback

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
        self.subtitle_label.pack(pady=(0, 40))

        # Continue Button
        self.continue_button = ctk.CTkButton(
            self,
            text="Enter",
            width=200,
            height=40,
            command=self.switch_callback
        )
        self.continue_button.pack(pady=20)

        # Footer
        self.footer_label = ctk.CTkLabel(
            self,
            text="© 2026 Recipe Encyclopedia Project",
            font=("Segoe UI", 12)
        )
        self.footer_label.pack(side="bottom", pady=20)


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Recipe Encyclopedia")
        self.geometry("900x600")
        ctk.set_appearance_mode("dark")  # You can change to "light" if needed
        ctk.set_default_color_theme("blue")

        # Start on Welcome Screen
        self.current_frame = None
        self.show_welcome_screen()

    def clear_frame(self):
        if self.current_frame is not None:
            self.current_frame.destroy()

    def show_welcome_screen(self):
        self.clear_frame()
        self.current_frame = WelcomeScreen(self, self.show_placeholder_main)
        self.current_frame.pack(fill="both", expand=True)

    def show_placeholder_main(self):
        """Temporary placeholder until you build the real navigation UI."""
        self.clear_frame()

        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True)

        label = ctk.CTkLabel(
            frame,
            text="Main Catalogue Placeholder\n(Navigation goes here)",
            font=("Segoe UI", 24, "bold")
        )
        label.pack(pady=200)

        back_button = ctk.CTkButton(
            frame,
            text="Back to Welcome",
            command=self.show_welcome_screen
        )
        back_button.pack(pady=20)

        self.current_frame = frame


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
