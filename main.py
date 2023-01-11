radio.set_group(123)

def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_a2():
    radio.send_string("SOS")
input.on_button_pressed(Button.A, on_button_pressed_a2)

def on_received_string(receivedString):
    pass
radio.on_received_string(on_received_string)

def on_received_string2(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string2)

