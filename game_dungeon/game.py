import pgzrun

TILE_SIZE = 64
HEIGHT = TILE_SIZE * 8
WIDTH = TILE_SIZE * 10

tiles = ['wall','road','blade','close_door',
        'diamond','door','hero','key']

maze = [[0,0,0,0,0,5,0,0,0,0],
        [1,1,1,4,0,4,1,0,1,0],
        [0,1,0,1,0,1,3,0,1,0],
        [0,1,0,1,1,0,1,1,1,0],
        [0,1,1,1,1,0,0,0,1,0],
        [0,1,0,0,1,1,1,0,1,0],
        [0,1,7,0,4,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0]]

player = Actor('hero',anchor=(0,0),pos=(0*TILE_SIZE,1*TILE_SIZE))
blade = Actor('blade',anchor=(0,0),pos=(1*TILE_SIZE,4*TILE_SIZE))
blade.xv = -1

def draw():
    screen.clear()
    screen.fill(color=(200,100,0))
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            tile = tiles[maze[row][col]]
            screen.blit(tile,(x,y))
    player.draw()
    blade.draw()
     

def on_key_down(key):
    # player movement
    row = int(player.y // TILE_SIZE)
    col =  int(player.x // TILE_SIZE)
    if key == key.UP:
        row = row-1    
    if key == key.DOWN:
        row = row+1
    if key == key.LEFT:
        col = col-1    
    if key == key.RIGHT:
        col = col+1
    tile = tiles[maze[row][col]]
    if tile !='wall':
        x = col * TILE_SIZE
        y = row * TILE_SIZE
        animate(player,duration=.1, pos=(x,y))
    if tile =='door':
        print('well done, you won')
        x = col * TILE_SIZE
        y = row * TILE_SIZE
        animate(player,duration=.1, pos=(x,y))

    # enemy movement
    row = int(blade.y / TILE_SIZE)
    col =  int(blade.x / TILE_SIZE)
    col = col + blade.xv
    tile = tiles[maze[row][col]]
    print(row,col,tile)
    if tile != 'wall':
        x = col * TILE_SIZE
        y = row * TILE_SIZE
        animate(blade,duration=.1, pos=(x,y))
    else:
        blade.xv = blade.xv * -1
    if blade.colliderect(player):
        print('you died')
        exit()

pgzrun.go()

