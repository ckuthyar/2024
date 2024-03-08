for j in range(0,12,1):
    
    for i in range(0,12,1):
        angle=(90-j*30)+i*30-i*2.5
        print(angle%360)
    print()
