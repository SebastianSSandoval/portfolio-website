import reflex as rx
from reflex.style import toggle_color_mode


class State(rx.State):
    """The app state."""

    pass


css: dict = {
    "app": {
        "_dark" :{
            "bg": "#15171b"
        }
    },
    
    "header": {
        "width": "100%",
        "height": "50px",
        "padding": [
            "1rem 1rem",
            "1rem 1rem",
            "1rem 1rem",
            "1rem 8rem",
            "1rem 8rem",
        ],
        "transition": "all 550ms ease",
    },
    "main":{
        "property":{
            "width": "100%",
            "height": "84vh",
            "padding" : "15rem 0rem",
            "align_items": "center",
            "justify_content" : "start",
        },
    },
}


class Header:
    def __init__(self) -> None:
        self.header: rx.Hstack = rx.hstack(style=css.get("header"))
        self.email: rx.Hstack = rx.hstack(
            rx.box(rx.icon(tag="mail", _dark={
                   "color": "rgba(255,255,255,0.5)"})),
            rx.box(
                rx.text(
                    "ssandoval2024@gmail.com", _dark={"color": "rgba(255,255,255,0.5)"}
                )
            ),
            align_items="center",
            justify_content="center",
        )
        self.theme: rx.Component = rx.color_mode.button(
            _light={"color": "black"},
            _dark={"color": "white"},
        )

    def compile_component(self) -> list:
        return [self.email, rx.spacer(), self.theme]

    def build(self):
        self.header.children = self.compile_component()
        return self.header


class Main:
    def __init__(self) -> None:
        self.box: rx.Box = rx.box(width="100%")
        self.name: rx.Hstack = rx.hstack(
            rx.heading(
                "Hi - I'm Sebastian",
                font_size=["2rem", "2.85rem", "4rem", "5rem", "5rem"],
                font_weight="900",
                _dark = {
                    "background" : "linear-gradient(to right, #e1e1e1, #757575)", #not working
                    "background_clip" : "text",
                }
            ),
            rx.heading("👋", font_size=["2rem", "2.85rem", "4rem", "5rem", "5rem"]),
            spacing = "2",
        )

    def compile_desktop_component(self):
        return rx.tablet_and_desktop(
            rx.vstack(
                self.name,
                style=css.get("main").get("property"),
            ),
        )

    def build(self) -> None:
        self.box.children = [self.compile_desktop_component()]
        return self.box


@rx.page(route="/")
def landing() -> rx.Component:
    header: object = Header().build()
    main: object = Main().build()

    return rx.vstack(
        header,
        main,
        background="radial-gradient(circle, rgba(255,255,255,0.09) 2px, transparent 2px)",
        background_size="25px 25px",
    )


app = rx.App()
app.add_page(landing)
