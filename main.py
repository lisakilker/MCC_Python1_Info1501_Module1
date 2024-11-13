#Imports the class file
import rectangle

def main():
    #Gets user input
    length = float(input("Enter the length as a float: "))
    width = float(input("Enter the width as a float: "))

    #Calls the get/set values
    myRectangle = rectangle.Rectangle(length, width)

    #Prints the output
    print("The length is:", myRectangle.get_length())
    print("The width is:", myRectangle.get_width())
    print("The area is:", myRectangle.get_area())

#Call the main function to execute the program
if __name__ == "__main__":
    main()
