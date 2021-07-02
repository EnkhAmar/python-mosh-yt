running = True
is_started = False
while running:
    command = input("> ").upper()
    if (command == "HELP"):
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "START":
        if is_started:
            print("Car has already started")
        else:
            is_started = True
            print("Car started... Ready to go!")
    elif command == "STOP":
        if not is_started:
            print("Car has already stopped")
        else:
            is_started = False
            print("Car stopped.")
    elif command == "QUIT":
        running = False
    else:
        print("I don't understand that...")