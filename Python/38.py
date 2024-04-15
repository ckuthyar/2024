def seatSelect():
    cols=[]
    rows=[]
    for i in range(1,21,1):
        cols.append(i)
    for i in range(65,65+26,1):
        rows.append(chr(i))
    for j in range(0,26,1):
        for i in range(0,26,1):
            row1=rows[j]+rows[i]
            rows.append(row1)   
    print(cols)
    print(rows)
seatSelect()
