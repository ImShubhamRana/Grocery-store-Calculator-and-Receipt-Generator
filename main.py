bill = 0
while True:
    userInput = input("Enter the item price or press q to quit: \n")
    if userInput != 'q':
        bill = bill + int(userInput)
        print(f"Your order total so far is {bill}")

    else:
        print(f"Your bill total is {bill}. Thanks for shopping from us")
        break