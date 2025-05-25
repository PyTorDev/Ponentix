import reflex as rx
from Ponentix.pages.index import index as index


class State(rx.State):
    pass


app = rx.App(
    theme=rx.theme(  # type: ignore
        appearance="light",
        has_background=False,
        radius="large",
        accent_color="violet",
    )
)
app.add_page(index)
