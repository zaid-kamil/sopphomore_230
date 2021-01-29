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
        [0,2,1,1,1,0,0,0,1,0],
        [0,1,0,0,1,1,1,0,1,0],
        [0,1,7,0,4,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0]]

player = Actor('hero',anchor=(0,0),pos=(0*TILE_SIZE,1*TILE_SIZE))

def draw():
    screen.clear()
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            print(row,col, maze[row][col])
            tile = tiles[maze[row][col]]
            screen.blit(tile,(x,y))
    player.draw()

def on_key_down(key):
    row = player.y // TILE_SIZE
    col =  player.x // TILE_SIZE
    if key == key.UP:
        row = row-1    
    if key == key.DOWN:
        row = row+1
    if key == key.LEFT:
        col = col-1    
    if key == key.RIGHT:
        col = col+1
    player.x = col * TILE_SIZE
    player.y = row * TILE_SIZE


pgzrun.go()

