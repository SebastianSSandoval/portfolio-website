import  reflex as rx

def navbar():
    return rx.chakra.hstack(
        rx.text("Salvador Sandoval"),
        rx.color_mode.button(rx.color_mode.icon(), align="right"),
        justify="between",
        width="100%",
    )