radio.setGroup(123)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a2() {
    radio.sendString("SOS")
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    
})
radio.onReceivedString(function on_received_string2(receivedString: string) {
    basic.showString(receivedString)
})
