chess = [[0,0,0],
         [1,0,1],
         [0,0,0]]  #works on greater size

rooks_positions = []
for i in range(len(chess)):
    for j in range(len(chess[i])):
        if chess[i][j] == 1:
            rooks_positions.append([i,j])

for i in rooks_positions:
    for j in rooks_positions:
        if i == j:
            continue
        else:
            if i[0] == j[0] or i[1] == j[1]:
                print(f"Rook can kill: {i,j}")
