def create_phone_number(numbers):
    # Check if the length of the array is correct
    if len(numbers) != 10:
        return "Invalid input: Array must contain 10 integers."

    # Convert the first three numbers to a string in the format "(XXX)"
    first_part = ''.join(map(str, numbers[:3]))
    first_part = f"({first_part})"

    # Convert the next three numbers to a string in the format " XXX-"
    second_part = ''.join(map(str, numbers[3:6]))
    second_part = f" {second_part}-"

    # Convert the last four numbers to a string in the format "XXX"
    third_part = ''.join(map(str, numbers[6:]))

    # Concatenate all parts to form the phone number string
    phone_number = first_part + second_part + third_part
    return phone_number

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(numbers))  # Output should be "(123) 456-7890"


# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
# => returns "(123) 456-7890"


#numeros=(input=str([0,1,2,3,4,5,6,7,8,9]))
#def telefono(numeros):
#    return (str(numeros[0]) + str(numeros[1]) + str(numeros[2]) + str(numeros[3]) + str(numeros[4]) + str(numeros[5]) + str(numeros[6]) + str(numeros[7]) + str(numeros[8]) + str(numeros[9])) 
    
# print ("El número de teléfono es: (" + telefono([0],[1],[2]) + ") + " + telefono([3],[4],[5]) + "-" + telefono([6],[7],[8],[9]))
    