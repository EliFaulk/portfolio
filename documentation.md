## Summary
My project is a retro version of battleship, displayed on a 12 x 12 grid of RGB LED lights and controlled with a number pad controller. To move the cursor of the game, use the numbers 2, 4, 6, and 8 as directions, and the number 7 as the select/place button. The color red represents areas where ships are, and the color blue indicates a barren piece of ocean with no ship. 
#### Materials
- Raspberry Pi 4
- Unicorn Hat HD RGB Matrix 16x16
- USB number pad

#### Wiring & Setup
This project has no breadboard for circuitry, and only uses the Unicorn Hat. To set up the Raspberry Pi, attach it to the pins, oriented laying over the Raspberry Pi.
Once the Raspberry Pi is turned on, the program should run automatically. If the program is running, the board will display a white square. 

## ADC (Analog to Digital Converter)
The MCP3008 is an ADC, or a chip that converts analog data to digital data. Analog data is constantly remeasured and changing data, or data related to real-world features. Time is an example of analog data, or the rotation of a knob on a device. To measure analog data, a constant voltage is taken and converted into digital data that the computer can read. 
![[MCP3008 Diagram.png]]
The left side of the MCP3008 are individual channels to which analog voltage should be sent to. The right side consists of the following:
- **Vdd/Vcc (supply voltage)**: the chip's power supply
- **VREF** (reference voltage): the chip's reference for voltage/analog data
- **Analog Ground**: ground for the VREF
- **Serial Clock**: provides clock signal for SPI communication
- **Serial Data Out**: outward transmission of SPI communication
- **Serial Data In**: inward transmission of SPI communication
- **Chip Select/Shutdown**: connected to a GPIO pin or MCU for turning on/off the IC
- **Digital Ground**: ground for circuit

## Unicorn Hat HD (Display Screen)
A hat is an add-on board that can be attached to the Raspberry Pi. The Unicorn Hat that I'm using is a 16x16 RGB LED grid, totaling to 256 lights. 
![Unicorn Hat HD](https://github.com/user-attachments/assets/6749bfdd-f71c-4d72-8516-5a1990a23456)

The *unicornhathd* library in Python contains all of the functions for operating the lights of the LED matrix.
| Function | Parameters | Usage |
| --- | --- | --- |
| set_pixel(x, y, red, green, blue) | The coordinates of the light on the grid (x and y) and the RGB color combination for that light | Set a single light's color on the Unicorn Hat |
| show() | NONE | Using parameters from the set_pixel() function, change the light's color |
| clear() | NONE | Turns off all lights on the Unicorn Hat |
| rotation(degree) | Degree of rotation by increments of 90s | Change orientation of the coordinate grid for the LED matrix |


## Sources
Unicorn Hat HD Pinout Diagram: https://pinout.xyz/pinout/unicorn_hat_hd

Unicorn Hat HD Shop Page: https://shop.pimoroni.com/products/unicorn-hat-hd?variant=42496126730

Unicorn Hat HD Github: https://github.com/pimoroni/unicorn-hat-hd/tree/master

Unicorn Hat HD Text Example: https://github.com/pimoroni/unicorn-hat-hd/blob/master/examples/text.py

Unicorn Hat HD Function Reference: http://docs.pimoroni.com/unicornhathd/
