import json
File="D:\\10kcoders\\backend\\python\\cc\\data.json"
def load_data():
    try:
        with open(File, "r") as f:
            return json.load(f)
    except:
        return []   
    
def save_data(data):
    with open(File, "w") as f:
        json.dump(data, f, indent=4)
def AddCard():
    print("Adding Function is Executing.....")
    UserName=input("Enter UserName:")
    password=input("Enter Your password:")
    CreditCardNumber=int(input("Enter Your CreditCard Number:"))
    CreditCardlimit=float(input("Enter Your CreditCard limit:"))
    OutStanding=0
    Info={
        "Name":UserName,
        "password":password,
        "CCnum":CreditCardNumber,
        "CClimit":CreditCardlimit,
        "Outstanding":OutStanding
    }
    data=load_data()
    data.append(Info)
    save_data(data)

    print("Your CreditCard Added Successfully!")


def ShowCard():
    print("Showcard Function is Executing.....")

    data = load_data()

    if len(data) == 0:
        print("No Cards Available!")
        return

    print(f"\nTotal Cards Found: {len(data)}")

    for card in data:
      print(card)


def SpendingCard():
    print("SpendingCard Function is Executing.....")

    data = load_data()

    if len(data) == 0:
        print("No Cards Available!")
        return

    card_num = int(input("Enter Your Credit Card Number: "))
    
    for card in data:

        if card["CCnum"] == card_num:
            amount = float(input("Enter Spending Amount: "))

            available = card["CClimit"] - card["Outstanding"]

            if amount > available:
                print(f"Transaction Failed! Available Limit: {available}")
                return

            card["Outstanding"] += amount
            save_data(data)

            print(f"Transaction Successful!")
            print("Now Your CreditCard limit:",card["CClimit"]-card["Outstanding"])

            return

    print("Card Not Found!")

def PaytheBill():
    print("Pay Bill Function is Executing.............")
    data = load_data()

    if len(data) == 0:
        print("No Cards Available!")
        return

    card_num = input("Enter Your Credit Card Number: ")

    for card in data:
        if str(card["CCnum"]) == card_num:

            outstanding = card["Outstanding"]
            print(f"Your Current Outstanding Amount: {outstanding}")

            payment = float(input("Enter Payment Amount: "))

            if payment == outstanding:
                card["Outstanding"] = 0
                save_data(data)
                print("Bill Cleared! Outstanding = 0")
                return

            elif payment < outstanding:
                card["Outstanding"] -= payment
                save_data(data)
                print(f"Payment Successful! New Outstanding: {card['Outstanding']}")
                return

            else:
                extra = payment - outstanding
                card["Outstanding"] = -extra   
                save_data(data)
                print(f"Bill Cleared! Extra amount {extra} added as credit.")
                print(f"Your Outstanding is now: {card['Outstanding']} (credit balance)")
                return

    print("Card Not Found!")

def main():
    print("Enter 1 for Adding CreditCards,Enter 2 for Showing CreaditCards,Enter 3 for Spending CreditCards.Enter 4 for Paying ")
    ip=int(input("Enter Your Choice Number:"))
    if ip==1:
        AddCard()
    elif ip==2:
        ShowCard()
    elif ip==3:
        SpendingCard()
    elif ip==4:
        PaytheBill()
    else:
        print("Please Enter Corrcet Choice!")
main()