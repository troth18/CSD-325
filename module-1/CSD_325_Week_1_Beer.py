#User input validation function
def get_input(prompt):
    while True:
        try:
            #Prompt user for input
            bottles = int(input(prompt))
            #Checks if input is between 1 and 99
            if (1 <= bottles <=99):
                return bottles
            else:
                print("Input a number between 1 and 99")
        #Error handling for if user input is not an integer
        except ValueError:
            print("Invalid input")
#Main function
def main():
    #Gets user input from get_input function
    beer = get_input("Enter the number of beer bottles (1-99): ")
    #Checks if beer is > 0
    #If so, outputs song and decreases beer by 1
    while beer > 0:
        print (f"{beer} bottle(s) of beer on the wall, {beer} bottle(s) of beer.")
        beer -= 1
        print(f"Take one down, pass it around, {beer} bottle(s) of beer on the wall.")
    #Checks if beer is < 0
    #If so, outputs that user should buy more beer
    else:
        print("Time to buy more beer!")
#Calls the main() function
main()