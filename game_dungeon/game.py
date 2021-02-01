import pgzrun

TILE_SIZE = 64
HEIGHT = TILE_SIZE * 8
WIDTH = TILE_SIZE * 10

tiles = ['wall','road','blade','close_door',
        'diamond','door','hero','key']

maze = [[0,0,0,0,0,5,0,0,0,0],
        [1,1,1,4,0,4,1,0,1,1],
        [0,1,0,1,0,1,3,0,1,0],
        [0,1,0,1,1,0,1,1,1,1],
        [0,1,1,1,1,0,0,0,1,0],
        [0,1,0,0,1,1,1,0,1,1],
        [0,1,7,0,4,1,1,1,1,4],
        [0,0,0,0,0,0,0,4,1,4]]

player = Actor('hero',anchor=(0,0),pos=(0*TILE_SIZE,1*TILE_SIZE))
blade = Actor('blade',anchor=(0,0),pos=(1*TILE_SIZE,4*TILE_SIZE))

# settings
blade.xv = -1
unlock = 0 # the gate is locked
score = 0  # player score
go = 1     # game state
msg= ''    # no msg

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
    if unlock ==0:
        ds = 'closed'
    else:
        ds = 'open'
    
    screen.draw.text(f'score: {score}\t door: {ds}',(10,10),color='blue')
    screen.draw.text(msg,(TILE_SIZE*3,TILE_SIZE*3),color='red',fontsize=40)

def on_key_down(key):
    global msg
    try:
        if go == 1:
            # movement
            player_move(key)
            blade_move(key)
        if go == 2:
            msg = 'well done, you won'
        if go == 0:
            msg = 'GAME OVER !!!'
    except:
        pass

def player_move(key):
    global unlock  # this mean -> this variable is created out of fucntion
    global score
    global go
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
    if tile =='road' or tile =='diamond' or tile =='key': 
        x = col * TILE_SIZE
        y = row * TILE_SIZE
        animate(player,duration=.1, pos=(x,y))
    if tile =='door':
        go = 2
        x = col * TILE_SIZE
        y = row * TILE_SIZE
        animate(player,duration=.1, pos=(x,y))
    if tile == 'key':
        unlock = 1                              # logic for saying player has key
        maze[row][col] = 1 
    if tile == 'diamond':                              
        maze[row][col] = 1      
        score +=1                                         # change the key image to road , so we can say we picked the key
    if tile == 'close_door' and unlock == 1:    # if you have key
        maze[row][col] = 1
        x = col * TILE_SIZE
        y = row * TILE_SIZE
        animate(player,duration=.1, pos=(x,y))
    else:
        pass                                    # dont let the player move out
    print(tile,row,col)

def blade_move(key):
    # blade movement
    global go

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
        go = 0
        player.image = 'road' # dead player

pgzrun.go()

