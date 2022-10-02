userInput = ""

while True:
    userInput = input("> ").lower()
    if userInput == "start":
        print("Car started...Ready to go!")
    elif userInput == "stop":
        print("Car stopped")
    elif userInput == "help":
        helpMessage = """
        start - to start the car
        stop - to stop the car
        quit - to exit
        """
        print(helpMessage)
    elif userInput == "quit":
        break
    else:
        print("I don't understand that...")