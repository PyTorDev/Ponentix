import reflex as rx
from Ponentix.components.navbar import navbar as navbar
from Ponentix.components.footer import footer as footer


def index() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                navbar(),
                rx.box(
                    rx.card(
                        rx.vstack(
                            rx.heading(
                                "¡Bienvenido a Ponentix!",
                                size="9",
                                color_scheme="violet",
                            ),
                            rx.text(
                                "Gestiona tus oradores y ponencias facilmente con Ponentix.",
                                align="center",
                                size="5",
                            ),
                            rx.button("Cargar oradores en formato csv"),
                            align_items="center",
                        ),
                        width="100%",
                        margin="0 auto",
                        margin_bottom="1em",
                    ),
                    rx.card(
                        rx.center(
                            rx.list.ordered(  # type: ignore
                                rx.list.item(  # type: ignore
                                    "Crea la tabla de oradores, con sus tipos de ponencias y sus preferencias, o importa tu archivo csv",
                                    align="center",
                                ),
                                rx.list.item(  # type: ignore
                                    "Revisa los datos en la sección Gestión de Oradores",
                                    align="center",
                                ),
                                rx.list.item(  # type: ignore
                                    "Añade los eventos y las diferentes ponencias de cada uno con sus respectivos requisitos en la sección Gestión de Eventos",
                                    align="center",
                                ),
                                rx.list.item(  # type: ignore
                                    "Ve a la sección de asiganción automatica, pulsa asignar y revisa los resultados",
                                    align="center",
                                ),
                                rx.list.item(  # type: ignore
                                    "Exporta la tabla resultante con todo el trabajo hecho",
                                    align="center",
                                ),
                                rx.list.item(  # type: ignore
                                    "Si quieres mantener los datos de tus oradores y eventos, exporta los archivos csv",
                                    align="center",
                                ),
                            ),
                        ),
                        width="100%",
                        margin="0 auto",
                        align_items="center",
                        padding_y="5em",
                        padding_x="8em",
                    ),
                    margin_top="5em",
                ),
                rx.container(
                    footer(),
                    bg=rx.color("accent", 3),
                    padding="1em",
                    bottom="0px",
                    z_index="5",
                    min_width="100%",
                    max_height="5em",
                    margin="0 auto",
                    margin_top="1em",
                ),
                align_items="center",
                min_whidth="50%",
                height="100vh",
                justify="between",
            ),
            style={"overflow": "hidden"},
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                navbar(),
                rx.box(
                    rx.card(
                        rx.vstack(
                            rx.heading(
                                "¡Bienvenido a Ponentix!",
                                size="6",
                                color_scheme="violet",
                            ),
                            rx.text(
                                "Gestiona tus oradores y ponencias facilmente con Ponentix.",
                                align="center",
                                size="3",
                            ),
                            rx.button("Cargar oradores en formato csv"),
                            align_items="center",
                        ),
                        width="80%",
                        margin="0 auto",
                        margin_bottom="1em",
                    ),
                    rx.card(
                        rx.center(
                            rx.list.ordered(  # type: ignore
                                rx.list.item(  # type: ignore
                                    "Crea la tabla de oradores, con sus tipos de ponencias y sus preferencias, o importa tu archivo csv",
                                    align="center",
                                ),
                                rx.list.item(  # type: ignore
                                    "Revisa los datos en la sección Gestión de Oradores",
                                    align="center",
                                ),
                                rx.list.item(  # type: ignore
                                    "Añade los eventos y las diferentes ponencias de cada uno con sus respectivos requisitos en la sección Gestión de Eventos",
                                    align="center",
                                ),
                                rx.list.item(  # type: ignore
                                    "Ve a la sección de asiganción automatica, pulsa asignar y revisa los resultados",
                                    align="center",
                                ),
                                rx.list.item(  # type: ignore
                                    "Exporta la tabla resultante con todo el trabajo hecho",
                                    align="center",
                                ),
                                rx.list.item(  # type: ignore
                                    "Si quieres mantener los datos de tus oradores y eventos, exporta los archivos csv",
                                    align="center",
                                ),
                            ),
                        ),
                        width="80%",
                        margin="0 auto",
                        align_items="center",
                        padding_y="1em",
                        padding_x="1em",
                        margin_bottom="1em",
                    ),
                    margin_top="5em",
                ),
                rx.container(
                    footer(),
                    bg=rx.color("accent", 3),
                    padding="1em",
                    bottom="0px",
                    min_width="100%",
                    margin="0 auto",
                    margin_bottom="0px",
                ),
            ),
        ),
    )
