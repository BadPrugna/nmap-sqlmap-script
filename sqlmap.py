def trovadb():
    sql=open("sqlmap.txt", "r")
    for e in sql:
        if "back-end DBMS:" in e:
            e=str(e[15:])
            a=e.split(' ')
            db=a[0]
    sql.close()
    print(db)


def nomedb():
    l=[]
    p=open("sqlmap.txt", "r")
    for e in p:
        if "resumed:"in e:
            a=e.split(' ')
            b=a[(len(a)-1)]
            c=b.split('\n')
            d=c[0]
            l.append(d)
    print(l)
    p.close()
    
def tabelladb():
    scan=open("sqlmap.txt", "r")
    scan=scan.readlines()
    d={'Database':''}
    for e in scan:
        e=str(e)
        if e.startswith('Database'):
            ind=scan.index(e)
            d[scan[ind][10:]]=''
    print(d)
    
    
            
            
            
        
            
                





