while True:
    try:
        miles = float(input("Please enter the amount of miles driven: "))
        print()
        break
    except ValueError:
        print("You did not enter a number!")

def kilo():
    print("Would you like a precise number?")
    while True:
        try:
            precise = (input("Please enter either y/n: ")).lower()
            if precise in ["y", "yes"]:
                global kilometers
                kilometers = miles * 1.60934
                kilometers = round(kilometers, 6)
                print(f"If you drove {miles} miles, you would've driven {kilometers} kilometers.")
                break
            elif precise in ["n", "no"]:
                kilometers = miles * 1.6
                print(f"If you drove {miles} miles, you would've driven {kilometers} kilometers.")
                break
        except ValueError:
            print("You did not enter either y/n.")
kilo()
