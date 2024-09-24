while True:
    try:
        # Prompt user for the number of LEDs
        num_leds = int(input("Enter the number of LEDs to switch on (1-10): "))
        
        # Check if the number is within the valid range
        if 1 <= num_leds <= 10:
            # Turn on LEDs using a for loop
            for i in range(1, num_leds + 1):
                print(f"LED {i} is ON")
        else:
            print("Number out of range. Please enter a number between 1 and 10.")
            continue

    except ValueError:
        # Handle invalid input (e.g., if the user enters something that's not an integer)
        print("Invalid input. Please enter a number between 1 and 10.")
        continue

    # Prompt if user wants to start again
    restart = input("Do you want to start again? (n to stop, any other key to continue): ").lower()
    if restart == 'n':
        print("Program ended.")
        break
