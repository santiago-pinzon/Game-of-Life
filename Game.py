import random

testm = [[True, True, False],
         [True, False, False],
         [False, False, False]]
w = 20;
temp = [[True for x in range(w)] for y in range(w)]
Matrix = [[bool(random.getrandbits(1)) for x in range(w)] for y in range(w)]
#Matrix = testm
on = "⬤ "
off = "○ "

def main():
    run(5)
    #setupRand()

def disp():
    for i in range(w):
        for j in range(w):
            if Matrix[i][j]:
                print(on, end = ' ')
            else:
                print(off, end = ' ')
        print()
    print()

def run(num):
    for x in range(num):
        gen()
        disp()

def gen():
    for i in range(w):
        for j in range(w):
            test(i, j)
    for i in range(w):
        for j in range(w):
            Matrix[i][j] = temp[i][j]
    return Matrix

def test(i, j):
    if neighbors(i, j):
        temp[i][j] = True
    else:
        temp[i][j] = False

def neighbors(i, j):
    if count(i, j) == 3 or count(i, j) == 2 and Matrix[i][j]:
        return True
    else:
        return False


# i = vertical
# j = horizontal
def count(i, j):
    num = 0
    # top edge check
    if i > 0 and Matrix[i - 1][j]:
        num += 1
    # left edge check
    if j > 0 and Matrix[i][j - 1]:
        num += 1
    # bottom edge check
    if i < w - 1 and Matrix[i + 1][j]:
        num += 1
    # right edge check
    if j < w - 1 and Matrix[i][j + 1]:
        num += 1
    # top left corner
    if i > 0 and j > 0 and Matrix[i - 1][j - 1]:
        num += 1
    # bottom left corner
    if i < w - 1 and j > 0 and Matrix[i + 1][j - 1]:
        num += 1
    # top right corner
    if i > 0 and j < w - 1 and Matrix[i - 1][j + 1]:
        num += 1
    # bottom right corner
    if i < w - 1 and j < w - 1 and Matrix[i + 1][j + 1]:
        num += 1
    return num




main()