# Created: Hamza Salman
# Created on: October 2016
# Course: ICS3U
# this program calculates wether or not a year is a leap year.

import ui


def check_touch_up_inside(sender):
    year_number = int(view['year_textfield'].text)

    if year_number % 100 == 0:
        if year_number % 400 == 0:
            view['output_label'].text = str(year_number) + ' is a leap year'
        else:
            view['output_label'].text = str(year_number) + ' is not a leap year'
            
    if year_number % 4 == 0:
        view['output_label'].text = str(year_number) + ' is a leap year'
    else:
        view['output_label'].text = str(year_number) + ' is a not leap year'

view = ui.load_view()
view.present('full_screen')

