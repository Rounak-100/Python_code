command=""
started=False
stopped=True
while True:
    command=input("> ").lower()
    if command=="start":
        if started==True:
            print("car is already started.")
        else:
            started=True
            stopped=False
            print("car stared...")
    elif command=="stop":
        if stopped==True:
            print("car already stop.")
        else:
            stopped=True
            started=False
            print("car stopped.")
    elif command=="help":
        print('''
start- to start the car.
stop- to stop the car.
quit- to quit.
''')
    elif command=="quit":
        break
    else:
        print("choose correct option.")

    
        