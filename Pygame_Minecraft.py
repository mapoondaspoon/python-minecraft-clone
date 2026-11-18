#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minecraft Clone in Python - Built with Ursina Engine
Run this directly from VS Code terminal or as a standalone .py file

Controls:
- WASD: Move character
- Space: Jump  
- Shift+Z: Break blocks (left-click)
- Shift+X: Place blocks (right-click)
- 1-8 keys: Select block types
- Click to interact with world

To run from VS Code, install Ursina first:
pip install ursina
"""

from ursina import *
import math
import os

# Setup app settings - this runs in full screen by default
app = Ursina()

# Block textures using colors (can be replaced with real texture images)
block_colors = [
    (color.rgb(34, 139, 34), "Grass"),     # Green grass block
    (color.rgb(139, 69, 19), "Dirt"),      # Brown dirt block
    (color.rgb(128, 128, 128), "Stone"),   # Gray stone block
    (color.rgb(139, 90, 43), "Wood"),      # Brown wood block
    (color.rgb(50, 50, 50), "Coal"),       # Black coal block
    (color.rgb(25, 135, 84), "Cyan"),      # Cyan/teal block
    (color.rgb(255, 69, 0), "Orange"),     # Orange block
    (color.rgb(173, 216, 230), "Sky Blue") # Light blue block
]

# Initialize hotbar with selected block
selected_block = 0

# World dimensions
world_width = 64
world_height = 32
world_depth = 64

def generate_world():
    """Generate terrain using sine waves for hills and valleys"""
    
    # Create ground layer
    for x in range(-world_width // 2, world_width // 2):
        for z in range(-world_depth // 2, world_depth // 2):
            # Calculate terrain height using sine waves for natural-looking hills
            noise = (math.sin(x * 0.1) + math.sin(z * 0.1)) / 3
            y_level = int((noise * 8))
            
            # Determine block type based on noise
            if abs(noise) < 0.2:
                color = color.rgb(34, 139, 34)  # Grass top
            elif abs(noise) > 0.5:
                color = color.rgb(139, 69, 19)  # Dirt on steep slopes
            else:
                color = color.rgb(128, 128, 128)  # Stone in caves
                
            # Create grass block (2.5 units tall to look like a cube with grass top)
            Entity(
                mesh=box,
                scale=(1, 2.5, 1),
                position=(x, y_level - 1, z),
                color=color,
                texture='white_cube'  # Simple white texture as placeholder
            )

# Generate the world when game starts
generate_world()

class Player:
    """Player character with movement and interaction"""
    
    def __init__(self):
        self.position = Vector3(0, 5, 0)  # Start at center of world
        self.speed = 7
        self.jump_velocity = 12
        
        # Create player model (cube for simplicity)
        self.model = Entity(
            parent=camera,
            model='cube',
            scale=0.8,
            color=color.rgb(100, 149, 237),  # Blue shirt
            position=self.position,
            rotation=(0, -90, 0)
        )
        
        # Setup collision detection
        self.collider = BoxCollider(self.model, box=(-0.6, -0.6, -0.6))

# Create player character
player = Player()

def click():
    """Handle left and right clicks for block breaking/placing"""
    
    # Get mouse position in world coordinates
    mouse_position = cursor.worldPosition
    
    # Left click: Remove block at clicked position
    if not held and 'left' in keys:
        # Find and delete any blocks at the clicked position
        for entity in entities:
            if isinstance(entity, Entity):
                if abs(entity.position - mouse_position) < 1.5:
                    entity.delete()
                    break
    
    # Right click: Place block at clicked position
    elif not held and 'right' in keys:
        selected_block = (selected_block + 1) % len(block_colors)
        if selected_block == 0:
            return
        
        # Place a new block slightly offset from mouse
        new_block = Entity(
            mesh=box,
            scale=(1, 2.5, 1),
            position=mouse_position + Vector3(-0.5, 0, -0.5),
            color=block_colors[selected_block][0],
            texture='white_cube'
        )

# Bind click events to camera (for mouse interaction)
cursor.worldPosition = camera.position

def key_press(key):
    """Handle hotbar selection"""
    
    # Map numbers 1-8 to block selections
    if 'key_' in str(key):
        key_num = int(str(key).replace('key_', '')) - 1
        selected_block = min(max(key_num, 0), len(block_colors) - 1)

# Bind keys for movement and interaction
app.keys['space'].pressable = True  # Jump
app.keys['shift'].pressable = False  # Hold shift for interactions

app.run()  # Start the game!