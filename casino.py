def gamble(q, s1, s2, s3):
    plays=0
    play=1
    while q>0:
        print(q)
        if play==1:
            s1+=1
            q=q-1
            plays=plays+1
            if s1 == 35:
                q+=30
                s1==0
            play=2
        elif play==2:
            s2+=1
            q=q-1
            plays=plays+1
            if s2==100:
                q+=60
                s2==0
            play=3
        elif play==3:
            s3+=1
            q=q-1
            plays=plays+1
            if s3==10:
                q+=9
                s3==0
            play=1
    print (plays)
gamble(77, 4, 9, 3)