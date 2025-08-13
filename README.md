# Wolfenstein 3D Reimplementation

<img src="https://github.com/user-attachments/assets/1c4f29d9-55a0-46e8-aead-67c5d112de8c" width=350/>

An in-progress, from-scratch, reimplementation of the FPS-genre pioneering game, [_Wolfenstein 3D_](https://en.wikipedia.org/wiki/Wolfenstein_3D), released by id Software in 1992, in Rust.
The goal is to reimplement all of the game's original functionality, as well as potentially add custom features like networked multiplayer.

## Current Engine Demo
https://github.com/user-attachments/assets/79e0a8ee-d1db-447c-99e2-ce526b7e7d25

### Remaining Features to Implement
- [ ] Enemy AI
- [ ] More weapons
- [ ] WAD parser
- [ ] Minimap
- [ ] Networked multiplayer _(aspirational)_
- [ ] Compile to [WebAssembly](https://rustwasm.github.io/docs/book)

### Completed
- [x] Raycasting
- [x] Texture mapping
- [x] Sprites (objects & enemies)
- [x] Doors
- [x] Controls (WASD, arrow keys, mouse) 
- [x] Custom map creation
- [x] General sprite animation system
- [x] Walking enemies
- [x] Shooting at enemies

## macOS Build Instructions
```
brew install sdl2 sdl2_image
```
Might need these in your `~/.zshrc`:
```
export LIBRARY_PATH="$LIBRARY_PATH:/opt/homebrew/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/usr/local/lib"
```
Then, from the root of this repo:
```
cargo run --release
```
## Controls
- `W` `A` `S` `D` to move around
- Mouse (or trackpad) to look around
- Left mouse click to shoot
- `Space` to open doors
- `~` to unlock/relock mouse from game window
- `Esc` to quit game

## What is written from scratch, what isn't
The core game logic and the rendering algorithm are written from scratch. The things not written from scratch are opening a window, putting pixels into it, reading mouse and keyboard inputs, managing textures, GPU-accelerated texture scaling, and doing all this in a cross-platform manner. To do all this for me, I'm using the excellent [SDL](https://github.com/libsdl-org/SDL) library. Doing all these tasks from scratch as well would be an interesting challenge, but I feel that would stray from the scope of the project.

## Credits & Disclaimer
As this is a reimplementation of a classic game, I'd like to state the obvious and say that this isn't "my" game. It is id Software's game, released by them in 1992. The entire concept of the game, the design, the mechanics, all of the artwork, is most definitely not my creation, it is theirs.

My creation and original work in this project lies purely in the technical realm of writing the code to replicate the workings of the game (hence, a reimplementation); all the logic and algorithms required. This is a purely educational pursuit for myself, I'm not trying to make any money off this (and if I tried, I'd have a lawsuit on my hands).

I found all the original artwork from the game [here](https://www.spriters-resource.com/pc_computer/wolfenstein3d/).
