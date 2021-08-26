fail = []
breaker = True
temporary = []

while True:
    try:
        target = int(input("Reichweite eingeben:"))
    except:
        pass

    for i in range(1,target+1):
        breaker = True
        current = i
        while breaker:
            if i % 2 == 0:
                i = i/2
            else: 
                i = i*3+1
            temporary.append(i)
            try:
                if temporary[-2:] == [1.0,4.0]:
                    fail.append(current)
                    breaker = False
                    temporary.clear()
            except:
                print("Array not long enough!")

    print(fail)
    print("{} von {} getesteten Zahlen sind in die Collatz-Endlosschleife gelaufen.".format(len(fail), target))
        


        