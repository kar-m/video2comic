# chat/components/navbar.py

import reflex as rx
from chat.state import State


def sidebar_chat(chat: str) -> rx.Component:
    """A sidebar chat item."""
    return rx.drawer.close(
        rx.hstack(
            rx.button(
                chat,
                on_click=lambda: State.set_chat(chat),
                width="80%",
                variant="surface",
            ),
            rx.button(
                rx.icon(
                    tag="trash",
                    on_click=State.delete_chat,
                    stroke_width=1,
                ),
                width="20%",
                variant="surface",
                color_scheme="red",
            ),
            width="100%",
        )
    )


def sidebar(trigger) -> rx.Component:
    """The sidebar component."""
    return rx.drawer.root(
        rx.drawer.trigger(trigger),
        rx.drawer.overlay(),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    rx.heading("API Keys", size="md", mb="4"),
                    rx.input(
                        value=State.OPENAI_API,
                        on_change=State.update_openai,
                        placeholder="Enter OPENAI API here...",
                    ),
                    rx.input(
                        value=State.GEMINI_API,
                        on_change=State.update_gemini,
                        placeholder="Enter GEMINI API here...",
                    ),
                    rx.input(
                        value=State.STYLE_API,
                        on_change=State.update_style,
                        placeholder="Enter STYLE API here...",
                    ),
                    spacing="4",
                    align_items="stretch",
                ),
                top="0",
                left="0",
                height="100vh",
                width="320px",
                padding="2em",
                background_color="white",
                shadow="lg",
            )
        ),
        direction="left",
    )


def navbar() -> rx.Component:
    """The navbar component."""
    return rx.box(
        rx.hstack(
            rx.hstack(
                sidebar(
                    rx.button(
                        rx.hstack(
                            rx.icon(
                                tag="sliders-horizontal",
                                size=16,
                                color=rx.color("mauve", 12),
                            ),
                            rx.text("API Keys", color=rx.color("mauve", 12)),
                            spacing="2",
                        ),
                        background_color=rx.color("mauve", 6),
                        padding="8px 16px",
                        border_radius="8px",
                    )
                ),
                align_items="center",
            ),
            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding_x="2em",
        ),
        width="100%",
        backdrop_filter="auto",
        backdrop_blur="lg",
        padding_y="12px",
        border_bottom=f"1px solid {rx.color('mauve', 3)}",
        background_color="rgba(255, 255, 255, 0.9)",
        position="sticky",
        top="0",
        z_index="100",
    )
