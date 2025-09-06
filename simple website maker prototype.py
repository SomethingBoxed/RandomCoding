########################################################################################################################################
#
#         Author: Ren Rose      
#         Project Name: simple website maker 
#         Date: 10/08/25(made), 6/09/25(updated)
#         Version: prototype 
#
#
########################################################################################################################################

"""
intro
ask for file name
ask for website title
ask for main header
ask for smaller head or p
ask for picture and if so ask for link or provide empty img
ask to sign website(not done)
done

"""

import time

def intro():
    time.sleep(0.9)
    print("Welcome to my website making machine!")
    time.sleep(1)
    print("The steps are simple")
    time.sleep(0.9)
    print("First name your html file")
    time.sleep(0.9)
    print("Then name your website")
    time.sleep(0.9)
    print("Give it a heading with some paragraphs and images")
    time.sleep(1)
    print("Finally sign it and then you're done!")
    time.sleep(0.9)
    

intro()
file_name = input("What do you want your website file to be named?(html file): ") + ".html"
while True:
    try:
        file = open(file_name, "x")
        break
    except FileExistsError:     #prevents already existing files from being overwritten
        file_name = input("File name already exists! Please enter a new file name: ")  + ".html"

with open(file_name, "w") as file:
    file.write("<!doctype html>\n\n<html>\n")
    title = input("What do you want your website title to be?(tab text): ")
    file.write('    <head>\n        <meta charset="utf-8">\n\n        <title>' + str(title) + '</title>\n    </head>\n\n')
    main_head = input("What do you want your main heading to be?: ") 
    file.write("    <body>\n\n        <h1>" + str(main_head) + "</h1>\n\n")
    file.write("        <p>")
    lines = int(input("How many lines do you want in your main paragraph?: "))
    counter = 0
    while counter != lines:
        text_body = input("What do you want your main paragraph to be?: ")
        file.write(text_body + "<br>")
        counter += 1
    file.write("</p>\n")
    image = input("Would you like to put a imagine in your website?(y/n): ")
    if image == "y":
        img = input("Please provide a valid image link or leave it empty if you want to put your own image in afterwards: ")
        file.write("        <img src='" + str(img) + "'> ")
    file.write("\n\n    </body>\n\n</html>")
    file.close
