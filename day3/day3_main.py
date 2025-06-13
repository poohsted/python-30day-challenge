try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("That's not a valid integer.")
finally:
    print("Done checking user input.")
    