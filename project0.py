user = int(input())
if user < 1000:
    i = 1
    x = "  "
    print("+-+")
    print("| |")
    if user > 1:
        print("+-+-+")
    elif user ==1:
        print ("+-+")
    
    while i != user:
        print(x*i + "| |")
        if i+1 != user:
            print(x*i + "+-+-+")
        else:
            print (x*(i) + "+-+")
        i = i+1
