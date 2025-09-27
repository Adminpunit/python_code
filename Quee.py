l=[]
while True:
    c=int(input('''
    1. Insert/push the element in queue
    2. Delete/pop the Element
    3. Get the front item from the queue 
    4. Get the last item from the queue 
    5. Display Queue
    6. exit()
    '''))
    if c==1:
        n=input("Inset the Value:=")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Queue is empty")
        else:
            del l[0]
            print(l)
    elif c==3:
        if len(l)==0:
            print("Empty queue")
        else:
            print("First element of Queue:=",l[0])
    elif c==4:
        if len(l)==0:
            print("Empty queue")
        else:
            print("First element of Queue:=",l[-1])
    elif c==5:
        print("Queue is =",l)
    else:
        break