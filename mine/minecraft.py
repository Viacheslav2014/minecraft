from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

block_pick = (1)

y_c = [0, -1, -2]

def update():
    global block_pick

    
    if held_keys['right mouse'] or held_keys['left mouse']:
        hand.active()
    else:
        hand.passive()

    
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['5']: block_pick = 5
    if held_keys['6']: block_pick = 6
    if held_keys['7']: block_pick = 7
    if held_keys['8']: block_pick = 8
    if held_keys['9']: block_pick = 9
    if held_keys['0']: block_pick = 0


class Voxel(Button):
    def __init__(self, position, texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,5)),
            highlight_color = color.black10,
            scale = 1)
    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = 'pls')
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = 'stone')
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = 'tree')
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = 'glass')
                if block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, texture = 'brick')
                if block_pick == 6: voxel = Voxel(position = self.position + mouse.normal, texture = 'redstone')
                if block_pick == 7: voxel = Voxel(position = self.position + mouse.normal, texture = 'lapis')
                if block_pick == 8: voxel = Voxel(position = self.position + mouse.normal, texture = 'leave')
                if block_pick == 9: voxel = Voxel(position = self.position + mouse.normal, texture = 'real')
                if block_pick == 0: voxel = Voxel(position = self.position + mouse.normal, texture = 'dirt')

            if key == 'left mouse down':
                destroy(self)

class Sky(Entity):
    def __init__(self,):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = 'sky.png',
            scale = 9999,
            double_sided = True)
        
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'cube',
            texture = 'arm',
            scale = 0.3,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.4,-0.3))
        
    def active(self):
        self.position = Vec2(0.1,-0.2)
    
    def passive(self):
        self.position = Vec2(0.4,-0.3)

app = Ursina()

for z in range(25):
    for x in range(25):
        voxel = Voxel(position = (x,0,z), texture='pls')
        for y in y_c:
            if y == -1:
                voxel = Voxel(position = (x,y,z), texture='dirt')
            if y == -2:
                voxel = Voxel(position = (x,y,z), texture='stone')
player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()