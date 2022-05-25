# level_data
level_map_0 = [
'XXXXX    S    S   S       S       S    S          S    S       S   S     ',    
'X   X  S            S       S       S    S     S        S   S    S   S   ',
'X   X          S   S  S    S   S             S     S       S         S   ',
'X   X S    S      S     S         S    S      S        S       S       S ',
'X   X   S          S           S     S       S      S        S    S S    ',
'X   X       S          S   S            S        S        S            S ',
'X   X    S      S    S   S         S      S     S    S       S  S    S   ',
'X   X         S       S     S    S    S                 S          S     ',
'X   X  P   S        S        S      S       S      S       S    S     S  ',
'X   X   S      S          S       S   S    S          S        S         ',
'X  HX               S                         S      W     S        E S  ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    ']

level_map_1 = [
'S             S                 S             S    ',    
'    S                                              ',
'        S           S     S               S        ',
'   S            S               S                  ',
'     S                               S        S    ',
' S         S    X    S       S           S         ',
'     S          X                           S      ',
'           S    X        S        S      x         ',
'S P             X           x            X      S  ',
'       S        X  S        X   x        X  S      ',
'H               X           X   X  X  x  X    W   E',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map_2 = [
'S  S                   x    S                S            S   ',    
' H   x  S      x                       S               S      ',
' X S       x   X   S       S xx                  S            ',
'   x S              x  xxx              S               S     ',
' S               S               S                 S          ',
'    xxX    S             S         x   X   xx                 ',
'              X S     xxx    S                  S          S  ',
'   S          X                                       S       ',
'  P   S  X    X    S                   S                      ',
'         X    X            S               S             S    ',
'   S     X      x    x    x    x    x    x    x    x    W    E',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map_3 = [
'       x  Cx  x               S                      ',
' S    x  x  x  x     S                S   C          ',
'     xC  S   x  x        S             x  x          ',
'    x  x   Sx  x                S     x  x      S    ',
'H    x  x  x  x S  x   x             x  x            ',
'X     x  x  x  x  x   x   x   x     x  x  S          ',
'X S    x  x      x   x     x   x   x  x         S    ',
'X       x  x    x   x       x   x x  x       S       ',
'X   P          x   x   S     x   xC x  S             ',
'X             x   x       S   x   x  x               ',
'X    S       x C x  S          x     S     x     W  E',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map_4 = [
'                                      ',
'                                      ',
'                                      ',
'                                      ',
'                                      ',
'                                      ',
'                                      ',
'                                      ',
'  P                                   ',
'                                      ',
'H                          W         E',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map_5 = [
'X                                              X ',
'X                                              X ',
'X                                              X ',
'X                                              X ',
'X                                              X ',
'X                                              X ',
'X                                              X ',
'X                                              X ',
'X  P                                           X ',
'X                                              X ',
'XE    W                           H            X ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ']

level_map_6 = [
'                                              ',
'                                              ',
'                                              ',
'                                              ',
'                                              ',
'                                              ',
'                                              ',
'                                              ',
'  P                                           ',
'                                              ',
'                                 S         W  ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
#level status
tile_size = 80
screen_width = 1500
screen_height = len(level_map_0) * tile_size        # len(level_map) = row(행)의 개수

level_map = [
'                                                  X ',
'                                                  X ',
'                                                  X ',
'                                                  X ',
'                                                  X ',
'                                                  X ',
'                                                  X ',
'                                                  X ',
'  P                                               X ',
'                                                  X ',
'E                                              W   E',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ']

