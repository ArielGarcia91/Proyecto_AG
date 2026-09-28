# Prompt the user for an integer N
n = int(input("Enter a number: "))

# Initialize the accumulator variable to store the running total
total_sum = 0

# Initialize an empty list to store the sequence of numbers as strings
sequence_elements = []

# Utilize the range() function to generate numbers from 1 up to N (inclusive)
for i in range(1, n + 1):
    total_sum += i  # Add the current number 'i' to the accumulator
    sequence_elements.append(str(i))  # Store the number for formatting

# Join the sequence list with " + " and print the final formatted result
sequence_string = " + ".join(sequence_elements)
print(f"Result: {sequence_string} = {total_sum}")
