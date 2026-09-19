4-Season VGA and Chiptune ASIC Engine (tt_um_vga_seasons)
An interactive, hardware-efficient System-on-Chip (SoC) design built for Tiny Tapeout, featuring procedural graphics, real-time weather and environmental overrides, multi-channel chiptune audio, and gamepad-driven sprite control.

Overview and Key Features
Procedural 4-Seasons Graphics Engine: Renders full-screen Spring, Summer, Autumn, and Winter landscapes dynamically using combinational math, coordinate comparators, and frame counters. Zero external RAM or ROM is required, maximizing standard cell-count efficiency.

Interactive Environment Controls (ui_in): Live-toggle weather animations (rain, snow, waves, clouds), UFO cosmic modes, volcanic eruptions, thunderstorms, and earthquake screen-shaking effects.

Themed Chiptune Synthesizer: Features an 8-bit LFSR pseudo-random noise generator for thunder and crackle effects, alongside clock-divider square-wave synthesis tailored to play atmospheric seasonal drone melodies, sci-fi theremin sweeps, and the McDonald's jingle.

Mascots and Game Mode (ui_in[7]): Spawns detailed 32x32 pixel-art characters (Jollibee, Ronald McDonald, and a fully controllable Mario). Toggling Game Mode redirects the D-Pad arrow keys to drive Mario across the screen in real time.

Pin,Name,Description
ui_in[0],Season Bit 0 / D-Pad Up,Season selector bit 0 (or Mario Up in Game Mode)
ui_in[1],Season Bit 1 / D-Pad Down,Season selector bit 1 (or Mario Down in Game Mode)
ui_in[2],Animate Toggle / D-Pad Left,Enables weather motion (or Mario Left in Game Mode)
ui_in[3],UFO Mode / D-Pad Right,Triggers cosmic UFO overlay (or Mario Right in Game Mode)
ui_in[4],Volcano Eruption,Triggers dynamic volcanic flow pattern
ui_in[5],Thunderstorm,Generates flashing background lightning and audio static
ui_in[6],Earthquake Jitter,Applies coordinate offset shaking to the entire frame
ui_in[7],Mascots and Game Mode,"Spawns Jollibee, Ronald, and Mario; activates gamepad control"

Dedicated Outputs (uo_out -- VGA PMOD)
uo[0] / uo[5] -- VGA Red (Bits 0 and 1)

uo[1] / uo[6] -- VGA Green (Bits 0 and 1)

uo[2] / uo[7] -- VGA Blue (Bits 0 and 1)

uo[3] -- VGA Horizontal Sync (hsync)

uo[4] -- VGA Vertical Sync (vsync)

Bidirectional Pins (uio)
uio[0] -- Audio Output (PWM/Square-wave chiptune signal for a piezo buzzer or filtered speaker).

uio[1:7] -- Unused / Tri-stated.

How to Test and Operate
Hardware Setup: Connect a standard VGA monitor via a TinyVGA PMOD and attach a piezo speaker or RC-filtered amplifier to bi-directional pin uio[0].

Select Seasons: Use ui_in[1:0] to cycle through the four environments:

00 = Spring (Blue skies, green grass, blooming flowers)

01 = Summer (Bright sun, tropical waters, beach sand)

10 = Autumn (Warm amber tones, falling leaves)

11 = Winter (Deep blue night, snowfall)

Trigger Weather and Disasters: Flip switches [2] through [6] to layer on cloud animations, UFOs, volcano flows, thunder, or earthquakes.

Play Game Mode: Flip ui_in[7] ON. This spawns the character sprites and routes your keyboard or gamepad arrow keys directly to Mario, allowing you to move him around the screen while background chiptune melodies play.

Simulation and Testing
To run the RTL simulation using Cocotb and Icarus Verilog:

Bash
cd test
make -B
To view generated waveforms in GTKWave:

Bash
gtkwave tb.fst tb.gtkw

