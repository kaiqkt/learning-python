"""
while em Python
"""

x = 0
# while x <= 10:
#     if x == 3:
#         x = x + 1
#         break  # -> para o loop
#         # continue -> continua o loop
#
#     print(x)
#     x = x + 1

y = 0  # linha
while x < 10:
    y = 0
    while y < 5:
        print(f'({x},{y})')
        y += 1
    x += 1
