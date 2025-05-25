import reflex as rx


def footer_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium"), href=url)


def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)


def footer() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.heading("© 2025 Ponentix", size="4", weight="bold"),
                rx.spacer(),
                footer_item("By Ailab Studio", "/#"),
                rx.image(
                    src="/logo.png",
                    width="2.50em",
                    height="auto",
                ),
                rx.spacer(),
                footer_item("Privacy Policy", "/#"),
                footer_item("Terms of Service", "/#"),
                align_items="center",
            ),
            justify="between",
            align_items="center",
            width="100%",
            margin="0 auto",
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.heading("© 2025 Ponentix", size="4", weight="bold"),
                rx.spacer(),
                footer_item("By Ailab Studio", "/#"),
                rx.image(
                    src="/logo.png",
                    width="2.50em",
                    height="auto",
                ),
                rx.spacer(),
                footer_item("Privacy Policy", "/#"),
                footer_item("Terms of Service", "/#"),
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        bootom="0px",
        min_width="100%",
        margin="0 auto",
    )
