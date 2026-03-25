# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 19:04:28 2026

@author: melia
"""

#%% 1. Matrix of Palindromes

r, c = map(int, input().split())
alpha = "abcdefghijklmnopqrstuvwxyz"
for row in range(r):
    palindromes = []
    for col in range(c):
        first = alpha[row]
        middle = alpha[row + col]
        palindromes.append(first + middle + first)
    print(" ".join(palindromes))


#%% 2. Diagonal Difference

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
primary = sum(matrix[i][i] for i in range(n))
secondary = sum(matrix[i][n - 1 - i] for i in range(n))
print(abs(primary - secondary))


#%% 3. 2x2 Squares in Matrix

rows, cols = map(int, input().split())
matrix = []
for _ in range(rows):
    matrix.append(input().split())
count = 0
for r in range(rows - 1):
    for c in range(cols - 1):
        if (matrix[r][c] == matrix[r][c+1] ==
                matrix[r+1][c] == matrix[r+1][c+1]):
            count += 1
print(count)


#%% 4. Maximal Sum

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
best_sum = None
best_r, best_c = 0, 0
for r in range(n - 2):
    for c in range(m - 2):
        s = sum(matrix[r+dr][c+dc] for dr in range(3) for dc in range(3))
        if best_sum is None or s > best_sum:
            best_sum = s
            best_r, best_c = r, c
print(f"Sum = {best_sum}")
for dr in range(3):
    print(" ".join(str(matrix[best_r+dr][best_c+dc]) for dc in range(3)))


#%% 5. Rubik's Matrix

r, c = map(int, input().split())
matrix = [[r * c + col + 1 for col in range(c)] for r in range(r)]
# re-read r,c as local vars properly
R, C = r, c
matrix = [[(row * C) + col + 1 for col in range(C)] for row in range(R)]

n = int(input())
for _ in range(n):
    parts = input().split()
    idx, direction, moves = int(parts[0]), parts[1], int(parts[2])
    moves = moves % (R if direction in ('left', 'right') else C)
    if direction == 'left':
        matrix[idx] = matrix[idx][moves:] + matrix[idx][:moves]
    elif direction == 'right':
        matrix[idx] = matrix[idx][-moves:] + matrix[idx][:-moves]
    elif direction == 'up':
        col_vals = [matrix[row][idx] for row in range(R)]
        col_vals = col_vals[moves:] + col_vals[:moves]
        for row in range(R):
            matrix[row][idx] = col_vals[row]
    elif direction == 'down':
        col_vals = [matrix[row][idx] for row in range(R)]
        col_vals = col_vals[-moves:] + col_vals[:-moves]
        for row in range(R):
            matrix[row][idx] = col_vals[row]

val = 1
for row in range(R):
    for col in range(C):
        cur_r, cur_c = None, None
        for sr in range(R):
            for sc in range(C):
                if matrix[sr][sc] == val:
                    cur_r, cur_c = sr, sc
        if cur_r == row and cur_c == col:
            print("No swap required")
        else:
            print(f"Swap ({row}, {col}) with ({cur_r}, {cur_c})")
            matrix[cur_r][cur_c] = matrix[row][col]
            matrix[row][col] = val
        val += 1


#%% 6. Target Practice

n, m = map(int, input().split())
snake = input()
shot_r, shot_c, radius = map(int, input().split())

matrix = [[' '] * m for _ in range(n)]
idx = 0
for row in range(n - 1, -1, -1):
    if (n - 1 - row) % 2 == 0:
        for col in range(m - 1, -1, -1):
            matrix[row][col] = snake[idx % len(snake)]
            idx += 1
    else:
        for col in range(m):
            matrix[row][col] = snake[idx % len(snake)]
            idx += 1

import math
for row in range(n):
    for col in range(m):
        if math.sqrt((row - shot_r)**2 + (col - shot_c)**2) <= radius:
            matrix[row][col] = ' '

for col in range(m):
    for row in range(n - 2, -1, -1):
        if matrix[row][col] != ' ' and matrix[row + 1][col] == ' ':
            r2 = row + 1
            while r2 < n - 1 and matrix[r2 + 1][col] == ' ':
                r2 += 1
            matrix[r2][col] = matrix[row][col]
            matrix[row][col] = ' '

for row in matrix:
    print("".join(row))


#%% 7. Lego Blocks

n = int(input())
first = []
for _ in range(n):
    first.append(list(map(int, input().split())))
second = []
for _ in range(n):
    second.append(list(map(int, input().split())))

second.reverse()
fits = True
width = len(first[0]) + len(second[0])
for i in range(n):
    if len(first[i]) + len(second[i]) != width:
        fits = False
        break

if fits:
    for i in range(n):
        combined = first[i] + second[i]
        print("[" + ", ".join(map(str, combined)) + "]")
else:
    total = sum(len(row) for row in first) + sum(len(row) for row in second)
    print(f"The total number of cells is: {total}")


#%% 8. Radioactive Mutant Vampire Bunnies

n, m = map(int, input().split())
lair = [list(input()) for _ in range(n)]
moves = input()

pr, pc = next((r, c) for r in range(n) for c in range(m) if lair[r][c] == 'P')

outcome = None
final_r, final_c = pr, pc

for move in moves:
    lair[pr][pc] = '.'
    nr, nc = pr, pc
    if move == 'U': nr -= 1
    elif move == 'D': nr += 1
    elif move == 'L': nc -= 1
    elif move == 'R': nc += 1

    if nr < 0 or nr >= n or nc < 0 or nc >= m:
        final_r, final_c = nr, nc
        outcome = 'won'
        new_bunnies = []
        for br in range(n):
            for bc in range(m):
                if lair[br][bc] == 'B':
                    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        tr, tc = br+dr, bc+dc
                        if 0 <= tr < n and 0 <= tc < m and lair[tr][tc] == '.':
                            new_bunnies.append((tr, tc))
        for br, bc in new_bunnies:
            lair[br][bc] = 'B'
        break

    if lair[nr][nc] == 'B':
        final_r, final_c = nr, nc
        outcome = 'dead'
        lair[nr][nc] = 'B'
        new_bunnies = []
        for br in range(n):
            for bc in range(m):
                if lair[br][bc] == 'B':
                    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        tr, tc = br+dr, bc+dc
                        if 0 <= tr < n and 0 <= tc < m and lair[tr][tc] == '.':
                            new_bunnies.append((tr, tc))
        for br, bc in new_bunnies:
            lair[br][bc] = 'B'
        break

    pr, pc = nr, nc
    lair[pr][pc] = 'P'
    final_r, final_c = pr, pc

    new_bunnies = []
    for br in range(n):
        for bc in range(m):
            if lair[br][bc] == 'B':
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    tr, tc = br+dr, bc+dc
                    if 0 <= tr < n and 0 <= tc < m and lair[tr][tc] == '.':
                        new_bunnies.append((tr, tc))
    for br, bc in new_bunnies:
        lair[br][bc] = 'B'

    if lair[pr][pc] == 'B':
        outcome = 'dead'
        final_r, final_c = pr, pc
        break

for row in lair:
    print("".join(row))
print(f"{outcome}: {final_r} {final_c}")


#%% 9. Crossfire

rows, cols = map(int, input().split())
matrix = [[row * cols + col + 1 for col in range(cols)] for row in range(rows)]

line = input()
while line != "Nuke it from orbit":
    r, c, radius = map(int, line.split())
    for dr in range(-radius, radius + 1):
        tr = r + dr
        if 0 <= tr < rows and 0 <= c < len(matrix[tr]):
            matrix[tr] = [v for i, v in enumerate(matrix[tr]) if i != matrix[tr].index(matrix[tr][matrix[tr].index(matrix[tr][c]) if c < len(matrix[tr]) else -1]) or True]
    line = input()

# Simpler correct approach
rows2, cols2 = rows, cols
matrix2 = [[row * cols2 + col + 1 for col in range(cols2)] for row in range(rows2)]
line = input() if False else "Nuke it from orbit"  # already consumed

# Redo properly
import sys
rows, cols = map(int, input().split()) if False else (rows, cols)

# Clean implementation
matrix = [[r * cols + c + 1 for c in range(cols)] for r in range(rows)]
for line in iter(input, "Nuke it from orbit"):
    cr, cc, radius = map(int, line.split())
    to_remove = set()
    for dr in range(-radius, radius + 1):
        tr = cr + dr
        if 0 <= tr < rows:
            to_remove.add((tr, cc))
    for dc in range(-radius, radius + 1):
        tc = cc + dc
        if 0 <= tc < cols:
            to_remove.add((cr, tc))
    matrix = [
        [matrix[r][c] for c in range(len(matrix[r])) if (r, c) not in to_remove]
        for r in range(rows)
    ]
    # re-index columns after removal is complex; use value-based removal
matrix_vals = [[r * cols + c + 1 for c in range(cols)] for r in range(rows)]
destroyed = set()
for line in []:  # already read above
    pass

# Final clean version (self-contained):
def crossfire():
    rows, cols = map(int, input().split())
    matrix = [[r * cols + c + 1 for c in range(cols)] for r in range(rows)]
    for line in iter(input, "Nuke it from orbit"):
        cr, cc, radius = map(int, line.split())
        to_del = set()
        for dr in range(-radius, radius + 1):
            tr = cr + dr
            if 0 <= tr < len(matrix):
                if 0 <= cc < len(matrix[tr]):
                    to_del.add(matrix[tr][cc])
        for dc in range(-radius, radius + 1):
            tc = cc + dc
            if 0 <= cr < len(matrix) and 0 <= tc < len(matrix[cr]):
                to_del.add(matrix[cr][tc])
        matrix = [[v for v in row if v not in to_del] for row in matrix]
    for row in matrix:
        if row:
            print(" ".join(map(str, row)))

crossfire()


#%% 11. Parking System

R, C = map(int, input().split())
parking = [[False] * C for _ in range(R)]  # False = free

line = input()
while line != "stop":
    z, x, y = map(int, line.split())
    row = parking[z]
    if all(row[1:]):
        print(f"Row {z} full")
    else:
        if not row[y]:
            row[y] = True
            dist = 1 + y
            print(dist)
        else:
            best = None
            best_dist = float('inf')
            for col in range(1, C):
                if not row[col]:
                    d = abs(col - y)
                    if d < best_dist or (d == best_dist and col < best):
                        best_dist = d
                        best = col
            row[best] = True
            print(1 + best)
    line = input()
