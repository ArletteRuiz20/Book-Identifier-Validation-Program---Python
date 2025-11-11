#Arlette Ruiz
#aruiz24@student.gsu.edu

def isbn10(isbn9):
    total=0
    for i in range(9):
        total += int(isbn9[i])*(i+1)
    checksum = total % 11
    if checksum ==10:
        checksum="X"
    return isbn9 + str(checksum)

isbn9=input("Enter the first 9 digits of an ISBN as a string: ")

if len(isbn9) !=9:
    print("Incorrect input.It must have exact 9 digits")
else:
    print("The ISBN-10 number is ", isbn10(isbn9))