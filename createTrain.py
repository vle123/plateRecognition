import shutil,os
fichierSortie = open('positives.lst','w')
fichierNega = open('negative.txt','w')
for i in range(7481):
    t="00"
    final=""
    if i <=999:
        t+="0"
    if i <=99:
        t+="0"
    if i<=9:
        t+="0"
    t+=str(i)
    final+=t+".png "
    coord=[]
    f = open(t+".txt")
    c=""
    s=0
    c=""
    for l in f.readlines():
        
        l=l.split(" ")
        
        if l[0] in ["Car","Truck","Van"]:
            s+=1
            c+= str(int(float(l[4])))+" "+str(int(float(l[5])))+" "+str(abs(int(float(l[4]) - int(float(l[6])))))+" "+str(abs( int(float(l[5])) -int(float(l[7]))))+" "
    if s >0:
        final+=str(s)+" "+c[:-1]+"\n"
        fichierSortie.write(final)  
    else:
        shutil.move('../positive/'+t+'.png', '../negative/'+t+'.png')
        fichierNega.write(t+'.png'+"\n")
    f.close()
fichierNega.close()
fichierSortie.close()