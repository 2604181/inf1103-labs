total = 0
failed = 0
while True:
    user_input = input("Enter stock quantity (or 'quit' to quit): ")
    if user_input == 'quit':
        break
    if not user_input.isdigit():
        print("Error. Please enter a valid whole number.")
        failed += 1
        continue

    quantity = int(user_input)

    if quantity < 0:
        print("Error. Quantity cannot be negative.")
        failed += 1
        continue

    total += quantity

    if total > 500:
        print(f"Overstock Alert: Total inventory is ({total} units), which exceeds 500 units!")
        break

print("---- Inventory Audit Summary ----")
print(f"Total Units Processed: {total}")
print(f"Number of Failed/Rejected Entries: {failed}")
