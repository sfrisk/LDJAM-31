init python:
    fuel = 100.00
    fuel_difficulty = 10.00
    max_fuel = 100.00

    def fuel_guage(st, at):

        ui.frame(xfill=False, yminimum=None,  xalign=.02, yalign=.05)

        ui.vbox() # (name, "HP", bar) from (level, hp, maxhp)

        ui.text("Fuel", size=20)

        ui.hbox() # "HP" from bar
        ui.bar(max_fuel, fuel,
               max_fuel=150)

        ui.close()
        ui.close()

    def get_fuel_percentage():
        return int(fuel / max_fuel * 100)
