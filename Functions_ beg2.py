# using functions in Python


# define a function that adds numbers
def addnum(num1, num2, num3):
    result = num1 + num2 + num3
    return result


def main():
    # Main logic will go in here
    print("The main is running...")
    #call the addnum function
    result1 = addnum(3,5,1)
    print(result1)
    print(addnum(result1,1,1))
    addnum("egg","bread","potato")

# Call the main function
if __name__ == "__main__":
    main()
