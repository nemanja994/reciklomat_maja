Brojac = 0
POCETNI_EKRAN1 = images.create_big_image("""
    # # # . # # # . . .
        # . # . # . . . . .
        # # # . # # # . . .
        # # . . # . . . . .
        # . # . # # # . . .
""")
POCETNI_EKRAN2 = images.create_big_image("""
    # # # . # . # . # .
        # . . . # . # # . .
        # . . . # . # . . .
        # . . . # . # # . .
        # # # . # . # . # .
""")
POCETNI_EKRAN1.scroll_image(1, 200)
POCETNI_EKRAN2.scroll_image(1, 200)

def on_forever():
    basic.show_number(Brojac)
basic.forever(on_forever)
