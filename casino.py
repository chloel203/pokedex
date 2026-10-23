def gamble(q, s1, s2, s3):
    plays=0
    turn=1
    while q>0:
        q=q-1
        plays=plays+1
        if turn==1:
            s1+=1
            if s1 == 35:
                q+=30
                s1=0
            turn=2
        elif turn==2:
            s2+=1
            if s2==100:
                q+=60
                s2=0
            turn=3
        elif turn==3:
            s3+=1
            if s3==10:
                q+=9
                s3=0
            turn=1
    print (plays)
gamble(77, 4, 9, 3)