total = 0
failed = 0
while True:
    user_input = input("Enter stock quantity (or 'quit' to quit): ")
    if user_input == 'quit':
        break
    if not user_input.isdigit():
        print("Invalid input. Please enter a valid whole number.")
        failed += 1
        continue

    quantity = int(user_input)

