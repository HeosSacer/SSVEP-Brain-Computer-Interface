from pygame import Surface, Rect

def create(flag,a=5,b=5,w=500,h=400):
    k = w/a
    l = h/b
    surf = Surface((w, h))
    c = (0, 0, 0) if flag else (255, 255, 255)
    surf.fill(c)
    for i in range(0,a):
        for j in range(0,b):
            c = (255, 255, 255) if c == (0, 0, 0) else (0, 0, 0)
            r = Rect(k*i,l*j,k,l)
            surf.fill(c,r)
    return surf
