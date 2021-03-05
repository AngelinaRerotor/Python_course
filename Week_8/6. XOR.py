from operator import xor

print(
    *map(
        lambda x, y: xor(x, y),
        map(
            int, input().split()),
        map(
            int, input().split())
    )
)
