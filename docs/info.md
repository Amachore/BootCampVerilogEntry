<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

Explore the four seasons in vibrant retro style! This interactive digital mini-world dynamically changes its visuals and weather using pure hardware logic (no memory required). It features changing skies, animated snow, rain, waves, and clouds. You can trigger fun events like volcanic eruptions, thunderstorms, UFOs, and earthquakes, or toggle Gamepad mode to control Mario alongside fast-food mascots while listening to matching chiptune music.

## How to test

1. Connect a standard VGA monitor and an audio speaker/buzzer to your FPGA/Tiny Tapeout board using a PMOD adapter.
2. Use input switches (`ui_in`) to control the experience:
   - **Switches 0–1:** Change the season (Spring, Summer, Autumn, Winter).
   - **Switch 2:** Toggle weather animations (clouds, rain, snow, waves).
   - **Switch 3:** Trigger UFO / Cosmic Night mode.
   - **Switch 4:** Trigger Volcano Eruption.
   - **Switch 5:** Trigger Thunderstorm.
   - **Switch 6:** Trigger Earthquake screen shake.
   - **Switch 7:** Turn on Game Mode to spawn Mario and the mascots, then use your arrow keys to move Mario around the screen.

## External hardware

- VGA Monitor (connected via standard VGA PMOD)
- Speaker or Piezo Buzzer (connected to bidirectional audio output pin `uio[0]`)
- Gamepad or Push-buttons for `ui_in` / `uio_in` control
