# 🎮 Minecraft Clone in Python

A fully functional Minecraft-style voxel world built with Python's Ursina engine! Run it directly from VS Code.

## ✨ Features

- **3D Voxel World** - Walk around a procedurally generated terrain
- **Block Interactions** - Break blocks (left-click) and place new ones (right-click)
- **8 Block Types** - Switch between grass, dirt, stone, wood, coal, and colored blocks
- **First-Person Controls** - WASD movement + mouse look
- **Smooth Physics** - Jumping, collision detection, and terrain climbing

## 🚀 Quick Start from VS Code

### 1. Install Dependencies (one-time setup)

In your VS Code terminal (Ctrl+`):

```bash
pip install -r requirements.txt
# OR just: pip install ursina
```

### 2. Run the Game

```bash
python Pygame_Minecraft.py
```

Or press `F5` in VS Code to run with debugging!

## 🎮 Controls

| Key | Action |
|-----|--------|
| **W** | Move forward |
| **A** | Strafe left |
| **S** | Move backward |
| **D** | Strafe right |
| **Space** | Jump |
| **Shift + Left Click** | Break blocks |
| **Shift + Right Click** | Place new block |
| **1-8 keys** | Select block types |
| **ESC** | Pause menu / ESC to quit game |

## 🎨 Block Types (numbered 1-8)

1. **Grass** - Green surface blocks
2. **Dirt** - Brown earth
3. **Stone** - Gray stone
4. **Wood** - Brown tree trunk
5. **Coal** - Black ore block
6. **Cyan** - Teal colored blocks
7. **Orange** - Orange decorative blocks
8. **Sky Blue** - Light blue blocks

## 📁 Project Structure

```
MinecraftClone/
├── Pygame_Minecraft.py    # Main game code
├── requirements.txt       # Dependencies list
└── README.md             # This file
```

## 💡 How It Works

- **Ursina Engine**: Handles all 3D graphics, physics, and rendering
- **Procedural Generation**: World uses sine waves to create hills/valleys
- **Voxel System**: Each block is a 1x2.5x1 unit cube
- **Collision Detection**: Player can't walk through blocks or fall infinitely
- **Camera System**: First-person view with mouse look

## 🛠️ Troubleshooting

**"ModuleNotFoundError: No module named 'ursina'"?**
```bash
pip install ursina
```

**"No such file or directory"?**
Make sure you're running the command from inside `MinecraftClone/` folder!

**Graphics look weird?**
Try updating graphics drivers. Ursina uses OpenGL for rendering.

## 🔧 Advanced Customization

Want to change things? Edit `Pygame_Minecraft.py`:

- **Change world size**: Modify `world_width`, `world_height`, `world_depth` at line 38
- **Change colors**: Edit the `block_colors` list (lines 21-27)
- **Adjust player speed**: Change `self.speed = 7` to a different value
- **Add more blocks**: Add more entries to `block_colors` list

## 📝 Technical Details

- **Language**: Python 3.8+
- **Engine**: Ursina (built on pygame + OpenGL)
- **Window**: Runs in full-screen or windowed mode
- **Save System**: Current version generates world each time (no persistence yet)

## 🎯 Next Steps to Improve

Want to expand the game? Here are ideas:

1. **Add textures**: Replace `white_cube` with actual Minecraft textures
2. **World saving**: Use JSON to save/load terrain
3. **More blocks**: Add diamond ore, redstone, sand, snow, etc.
4. **Mobs**: Add pigs, cows, creepers (using Ursina sprites)
5. **Crafting system**: Make a crafting table interface
6. **Tools**: Add pickaxes, shovels with different breaking speeds

## 🆘 Need Help?

If you run into issues:

1. Check that Python is installed (`python --version`)
2. Verify Ursina installed correctly (`pip list | grep ursina`)
3. Try running `python Pygame_Minecraft.py` from VS Code terminal
4. Check that your graphics drivers are up to date

---

**Enjoy building your Minecraft clone! Happy coding! 🎉**