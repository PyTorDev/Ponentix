import reflex as rx


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium"), href=url)


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.png",
                        width="2.50em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Ponentix", size="7", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item(
                            "Inicio"
                        ),  # Poner dentro del item un rx.link("Inicio", href="/#")
                        rx.menu.item("Gestión de Oradores"),
                        rx.menu.item("Gestión de Eventos"),
                        rx.menu.item("Asignador automatico"),
                        rx.menu.item("Configuración"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
                width="100%",
                margin="0 auto",
            ),
            width="100%",
            margin="0 auto",
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.png",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Reflex", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item(
                            "Inicio"
                        ),  # Poner dentro del item un rx.link("Inicio", href="/#")
                        rx.menu.item("Gestión de Oradores"),
                        rx.menu.item("Gestión de Eventos"),
                        rx.menu.item("Asignador automatico"),
                        rx.menu.item("Configuración"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        position="fixed",
        top="0px",
        z_index="5",
        min_width="100%",
        margin="0 auto",
    )
