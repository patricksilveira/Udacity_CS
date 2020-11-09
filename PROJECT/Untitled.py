def countApplesAndOranges(s, t, a, b, apples, oranges):
    inApples = 0
    inOranges = 0
    for i in apples:
        if (a + i) >= s and (a + i) <= t:
            inApples += +1
    for i in oranges:
        if (b + i) >= s and (b + i) <= t:
            inOranges += +1
    print (inApples+"\n"+inOranges)



s=7
t=11
a=5
b=15
apples =(-2, 2, 1)
oranges=(5, -6)

countApplesAndOranges(s, t, a, b, apples, oranges)
