import reflex as rx
from reflex.style import toggle_color_mode
#from links import name, resume, githubLink


class State(rx.State):
    """The app state."""

    pass


dots: dict = {
    "@keyframes dots": {
        "0%": {"background_position": "0 0"},
        "100%": {"background_position": "40px 40px"},
    },
    "animation": "dots 4s linear infinite alternate-reverse both",
}

wave: dict = {
    "@keyframes wave": {
        "0%": {"transform": "rotate(25deg)"},
        "100%": {"transform": "rotate(-15deg)"},
    },
    "animation": " wave 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) infinite alternate-reverse both",
}

# CSS dictionary to keep track of objects, these include the
css: dict = {
    "app": {
        "_dark": {
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
    "main": {
        "property": {
            "width": "100%",
            "height": "84vh",
            "padding": "15rem 0rem",
            "align_items": "center",
            "justify_content": "start",
        },
    },
    "project_heading": {
        "property": {
            "width": "100%",
            "height": "42vh",
            "padding": "15rem 0rem",
            "align_items": "center",
        }
    }
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
                f"Hi - I'm {name}",
                font_size=["2rem", "2.85rem", "4rem", "5rem", "5rem"],
                font_weight="900",

                _dark={
                    "background": "linear-gradient(to right, #e1e1e1, #757575)",
                    "background_clip": "text",
                    "-webkit-background-clip": "text",
                    "-webkit-text-fill-color": "transparent"
                }
            ),
            rx.heading("👋", font_size=[
                       "2rem", "2.85rem", "4rem", "5rem", "5rem"],
                       style=wave,
                       ),
            spacing="2",
        )

        # self.spacer : rx.Spacer = rx.spacer(spacing = "2"),

        # method : create socials

        # method : create badges

        self.badge_stack_max: rx.Hstack = rx.hstack(spacing="1")
        self.badge_stack_min: rx.Vstack = rx.vstack(spacing="2")
        titles: list = ["Software Engineer",
                        "AI Developer", "Python Developer"]
        self.badge_stack_max.children = [
            self.create_badges(title) for title in titles]
        self.badge_stack_min.children = [
            self.create_badges(title) for title in titles]
        # FIXME
        # need to do the links
        """image link: will be stored locally
            page title: in the code
            actual link
            """
        self.bread_crumb_max: rx.Hstack = rx.hstack(spacing="1")
        self.bread_crumb_min: rx.Vstack = rx.vstack(spacing="2")
        data: list = [
            ["/github-circle.svg", "Git", githubLink],
            ["/github.png", "LinkedIn", "#"],
            ["/github.png", "Resume", resume],
        ]
        self.bread_crumb_max.children = [self.create_breadcrumb_item(
            path, title, url) for path, title, url in data]
        self.bread_crumb_min.children = [self.create_breadcrumb_item(
            path, title, url) for path, title, url in data]

        self.project_heading: rx.Heading = rx.heading(
            "Project list",
            font_size=["1.33rem", "1.9rem", "2.67rem", "3.33rem", "3.33rem"],
            font_weight="900",
            _dark={
                        "background": "linear-gradient(to right, #e1e1e1, #757575)",
                        "background_clip": "text",
                        "-webkit-background-clip": "text",
                        "-webkit-text-fill-color": "transparent"
            }
        )

        self.project_grid: rx.Grid = rx.grid(
        rx.foreach(
                rx.Var.range(9),
                #FIXME instead have each card be a button that links to each project
                lambda i: rx.card(f"Card {i + 1}", height="10vh"),
            ),
            columns = "3",
            spacing = "3",
            width = "80%",
            
    )


    def create_breadcrumb_item(self, path: str, title: str, url: str | None):
        return rx.link(
            rx.center(
                rx.image(
                    src=path,
                    width="24px",
                    height="24px",
                    _dark={"filter": "invert (1)"},
                ),
            ),
            title,
            href = url,
            _dark = {"color": "rgba(255,255,255,0.7)"},
            is_external = True,

        )

    def create_badges(self, title: str) -> None:
        return rx.badge(
            title,
            variant="solid",
            padding=["0.15rem 0.35rem ",
                     "0.15rem 0.35rem ",
                     "0.15rem 1rem ",
                     "0.15rem 1rem ",
                     "0.15rem 1rem ",
                     ],
        )

    

    def compile_desktop_component(self):
        return rx.tablet_and_desktop(
            rx.vstack(
                self.name,
                rx.spacer(spacing="1"),
                self.badge_stack_max,
                rx.spacer(spacing="1"),
                self.bread_crumb_max,
                rx.spacer(spacing="1"),
                self.project_heading,
                rx.spacer(spacing="1"),
                self.project_grid,
                # self.project board

                style=css.get("main").get("property"),
            ),
        )

    def compile_mobile_component(self):
        return rx.mobile_only(
            rx.vstack(
                self.name,
                rx.spacer(spacing="1"),
                self.badge_stack_min,
                rx.spacer(spacing="1"),
                self.bread_crumb_min,
                rx.spacer(spacing="1"),
                self.project_heading,
                rx.spacer(spacing="1"),
                self.project_grid,
                style=css.get("main").get("property"),


            )
        )

    def build(self) -> None:
        self.box.children = [
            self.compile_desktop_component(), self.compile_mobile_component()]
        return self.box


@rx.page(route="/")
def landing() -> rx.Component:
    header: object = Header().build()
    main: object = Main().build()

    return rx.vstack(
        header,
        main,
        _light={
            "background": "radial-gradient(circle, rgba(0,0,0,0.35) 1px, transparent 1px)",
            "background_size": "25px 25px",
            "background_position": "0 0",

        },
        _dark={
            "background": "radial-gradient(circle, rgba(255,255,255,0.09) 2px, transparent 2px)",
            "background_size": "25px 25px",
            "background_position": "0 0",

        },


        style=dots,
    )


app = rx.App()
app.add_page(landing)
