########################################################################################################################################
#
#         Author: Ren Rose      
#         Project Name: text file maker 
#         Date: 30/07/25(made), 8/08/25(updated)
#         Version: prototype 
#
#
########################################################################################################################################

"""
intro
open text file
add file content
check if sure about closing
close file and save as name
make recallable function to make new file


"""
import time
def intro():
    print("Welcome to text file maker!") 
    time.sleep(0.5)
    print("The process is pretty simple")
    time.sleep(0.5)

def newfile():
    intro()
    name = input("Please enter your file name: ")
    filename = name + ".txt"    #allows user's input to be used as a file name
    while True:
        try:
            file = open(filename, "x")
            break
        except FileExistsError:     #prevents already existing files from being overwritten
            name = input("File name already exists! Please enter a new file name: ")
            filename = name + ".txt"   

    with open(filename, "w") as file:   #writes the input into the file
        file_content = input("Type what you want to be in your text file: ")
        file.write(file_content)
        extra = input("Do you want to go to the next line?(y/n): ")
        while extra not in ("y","n"):       #error handling for extra lines
            extra = input("Invalid,do you want to go to the next line?(y/n): ")
        while extra == "y":     #writes the new input onto a new line
            file.write("\n")
            file_content2 = input("Type what you want to add to your text file: ")
            file.write(file_content2)
            extra = input("Do you want to go to the next line(y/n): ")
        file.close
    print("Processing...") 
    time.sleep(0.7)
    print("Done!")
    time.sleep(0.5)
    extra = input("Want to make a new file?(y/n): ")    #allows the user to make multiple text files without having to reload the program each time
    while extra not in ("y","n"):
        extra = input("Invalid, do you want to make a new file?(y/n): ")
    while extra == "y":
        newfile()

newfile()
