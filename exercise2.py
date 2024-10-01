from math import sqrt, floor

tiles = int(input("Number of tiles: "))

answer = sqrt(tiles)
answer = floor(answer)

print(f"Largest square sidelength is {answer}")
