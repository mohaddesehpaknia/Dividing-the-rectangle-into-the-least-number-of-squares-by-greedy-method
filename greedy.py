def greedy(m,n,c):
    # agar tol va arz barabar shod axarin moraba ra entexab mikonim
    if m == n:
        print(f"{n}*{n}")
        print(c+1)
        return c
    # m ra zele bozorgtar dar nazar gerefteim
    if m < n:
        m, n = n, m
    m -= n 
    print(f"{n}*{n}")
    c +=1
    # faraxani tabe greedy
    greedy(m,n,c)
#run
x = int(input('lotfan tol zamin morede nazar ra vared konid:'))
y = int(input('lotfan arz zamin morede nazar ra vared konid:'))
greedy(x,y,0)
