# chat/chat.py

import reflex as rx
from chat.state import State
from chat.components import chat, navbar

# Constants for styling
COLORS = {
    "primary": "rgb(107,99,246)",
    "background": "#f5f5f5",
    "white": "white",
    "gray": "#666666",
}

STYLES = {
    "container": {
        "width": "100%",
        "max_width": "1200px",
        "margin": "0 auto",
        "padding": "2em",
        "min_height": "100vh",
        "background": COLORS["white"],
    },
    "header": {
        "width": "100%",
        "padding": "1em",
        "background": COLORS["white"],
        "border_bottom": f"1px solid {COLORS['background']}",
        "margin_bottom": "2em",
    },
    "button": {
        "background": COLORS["primary"],
        "color": COLORS["white"],
        "padding": "0.75em 1.5em",
        "border_radius": "8px",
        "font_weight": "500",
        "_hover": {"opacity": 0.9},
    },
    "outlined_button": {
        "background": COLORS["white"],
        "color": COLORS["primary"],
        "border": f"1px solid {COLORS['primary']}",
        "padding": "0.75em 1.5em",
        "border_radius": "8px",
        "font_weight": "500",
        "_hover": {"background": COLORS["background"]},
    },
}


def chat() -> rx.Component:
    """Display the processed images in a grid layout."""
    return rx.box(
        rx.cond(
            State.pdf_images,
            rx.flex(
                rx.foreach(
                    State.pdf_images,
                    lambda image: rx.box(
                        rx.image(
                            src=image,
                            border_radius="12px",
                            width="100%",
                            height="auto",
                            shadow="lg",
                        ),
                        padding="1em",
                        flex_basis="25%",  # 4 columns
                        min_width="250px",  # Minimum width before wrapping
                    ),
                ),
                flex_wrap="wrap",
                gap="4",
                width="100%",
            ),
            rx.center(
                rx.vstack(
                    rx.icon(
                        tag="image",
                        color=COLORS["gray"],
                        size=32,  # Fixed: Changed from "4em" to integer
                    ),
                    rx.text(
                        "No images processed yet",
                        color=COLORS["gray"],
                        font_size="1.1em",
                    ),
                    spacing="4",
                    padding="4em",
                ),
            ),
        ),
    )


def action_bar() -> rx.Component:
    """Enhanced action bar with better visual hierarchy and feedback."""
    return rx.vstack(
        rx.hstack(
            rx.upload(
                rx.button(
                    rx.hstack(
                        rx.icon(tag="upload", size=16),  # Fixed: Added integer size
                        rx.text("Select Video"),
                        spacing="2",
                    ),
                    **STYLES["outlined_button"],
                ),
                id="upload1",
                multiple=False,
                accept={
                    "video/mp4": [".mp4"],
                    "video/quicktime": [".mov"],
                },
                max_files=1,
                padding="0px",
            ),
            rx.hstack(
                rx.foreach(
                    rx.selected_files("upload1"),
                    lambda file: rx.hstack(
                        rx.icon(
                            tag="file", color=COLORS["primary"], size=16
                        ),  # Fixed: Added integer size
                        rx.text(file, color=COLORS["gray"]),
                        background=COLORS["background"],
                        padding="0.5em 1em",
                        border_radius="6px",
                    ),
                ),
            ),
            width="100%",
            spacing="4",
        ),
        rx.flex(
            rx.button(
                rx.hstack(
                    rx.icon(tag="cloud-upload", size=16),  # Fixed: Added integer size
                    rx.text("Upload"),
                    spacing="2",
                ),
                on_click=State.handle_upload(rx.upload_files(upload_id="upload1")),
                **STYLES["button"],
            ),
            rx.button(
                rx.hstack(
                    rx.icon(tag="settings", size=16),  # Fixed: Added integer size
                    rx.text("Process Video"),
                    spacing="2",
                ),
                on_click=State.get_pdf_,
                **STYLES["button"],
            ),
            rx.button(
                rx.hstack(
                    rx.icon(tag="download", size=16),  # Fixed: Added integer size
                    rx.text("Download Comic"),
                    spacing="2",
                ),
                on_click=rx.download(
                    url="/",
                    filename=State.output_path,
                ),
                **STYLES["button"],
                is_disabled=~State.output_path,
            ),
            gap="4",
            flex_wrap="wrap",
            width="100%",
        ),
        spacing="6",
        padding="2em",
        background=COLORS["background"],
        border_radius="12px",
        width="100%",
    )


def index() -> rx.Component:
    """Main page layout with navbar properly positioned."""
    return rx.box(
        rx.vstack(
            navbar(),  # Navbar at the top
            rx.box(  # Container for main content
                rx.vstack(
                    rx.heading(
                        "Video to Comic Converter",
                        size="lg",
                        color=COLORS["primary"],
                    ),
                    rx.text(
                        "Upload a video to convert it into a comic-style image sequence",
                        color=COLORS["gray"],
                    ),
                    action_bar(),
                    chat(),
                    spacing="6",
                    align_items="stretch",
                ),
                **STYLES["container"],
            ),
            width="100%",
            spacing="0",
            align_items="stretch",
        ),
        width="100%",
        min_height="100vh",
        background=COLORS["background"],
    )


# Create the app instance
app = rx.App()

# Add the index page to the app
app.add_page(index)
