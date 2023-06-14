print("Starting")

import board
import supervisor
import digitalio
import storage
import usb_cdc
import usb_hid

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers


keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.col_pins = (board.D2, board.D3, board.D4, board.D5, board.D6,)
keyboard.row_pins = (board.A3, board.A2, board.A1, board.A0, board.D9,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.MO(1)

keyboard.keymap = [
    # Base layer
    [
        KC.ESCAPE, KC.N1, KC.N2, KC.N4, KC.N5,
        KC.TAB,    KC.Q,  KC.W,  KC.N3, KC.R,
        KC.G,      KC.A,  KC.S,  KC.E,  KC.F,
        KC.LSHIFT, KC.Z,  KC.X,  KC.D,  KC.V,
        KC.LCTRL,  KC.LGUI, LOWER, KC.C, KC.SPACE,
    ],
    #Function layer
    [
        KC.GRAVE, KC.F1, KC.F2, KC.F4, KC.F5,
        KC.BSPACE, KC.T,  KC.Y,  KC.F3, KC.I,
        KC.ENTER, KC.O,  KC.P,  KC.U,  KC.J,
        _______,  KC.K,  KC.L,  KC.H,  KC.N,
        KC.M, KC.COMMA, _______, KC.B, KC.DOT,
    ],
]

if __name__ == '__main__':
    keyboard.go()
