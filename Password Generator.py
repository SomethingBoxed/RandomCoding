################################################################################
#
#
#   Programmer: RenRose
#   Date created: 05/05/2024
#
################################################################################

def split_and_swap(string):
    # Remove spaces from the string
    string = string.replace(" ", "")
    # Checks if input is longer than 5 letters and splits it into two
    if len(string) > 5:
        middle_index = len(string) // 2
        return string[middle_index:] + string[:middle_index]
    else:
        return string

password1 = input("Enter favourite color:").strip()
password2 = input("Enter favourite food:").strip()
password3 = input("Enter favourite animal:").strip()

# Split and swap strings longer than 5 characters
password1 = split_and_swap(password1)
password2 = split_and_swap(password2)
password3 = split_and_swap(password3)

# Check if input is empty
if password1 == "":
    print("Invalid input, try again")
    password1 = input("Enter favourite color:").strip()
    password1 = split_and_swap(password1)
if password2 == "":
    print("Invalid input, try again")
    password2 = input("Enter favourite food:").strip()
    password2 = split_and_swap(password2)
if password3 == "":
    print("Invalid input, try again")
    password3 = input("Enter favourite animal:").strip()
    password3 = split_and_swap(password3)

print("Password is:", password3 + password1 + password2)

