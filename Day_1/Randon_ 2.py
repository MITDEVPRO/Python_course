colums = 3
rows = 3

# Define the rows of the map using lists with emojis
line1 = ["⬜️", "⬜️", "⬜️"]
line2 = ["⬜️", "⬜️", "⬜️"]
line3 = ["⬜️", "⬜️", "⬜️"]

# Group the rows into a list representing the map
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")

# Prompt the user to enter the position where they want to put the 'X'
position = input("Enter your coordinates (e.g., B2): ")  # Example input: "B2"

# 🚨 Don't change the code above 👆

# Extract the column (letter) from the position and convert it to uppercase
column = position[0].upper()

# Extract the row (number) from the position and subtract 1 to convert it to a 0-based index
row = int(position[1]) - 1

# Convert the column to a 0-based index
# ord(column) gets the Unicode value of the letter, and ord('A') gets the Unicode value of 'A' (65)
# So, 'A' becomes 0, 'B' becomes 1, etc.
column_index = ord(column) - ord('A')

# Place an 'X' at the specified position on the map
map[row][column_index] = "X"

# 🚨 Don't change the code below 👇

# Print each line of the map to displb1bay the result
print(f"{line1}\n{line2}\n{line3}")

