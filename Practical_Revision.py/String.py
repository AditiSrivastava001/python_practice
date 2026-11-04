# Q1. Personal introduction
# Create a variable containing your full name.
# Perform the following:
# - Print your name in uppercase.
# - Print your name in lowercase.
# - Print your name using title case.
# - Print the total number of characters using len().

# Name = "Aditi Srivastava"

# print(Name.upper())
# print(Name.lower())
# print(Name.title())
# print(len(Name))

# Q2. Extract first and last name
# Extract and print:
# - First name
# - Last name
# Hint: Use split().

# Name = "Aditi Srivastava"

# print(Name.split())

# Count characters  (Need to do it again)
# message = "Python is very interesting"
# Find and print:
# - Total characters.
# - Total characters excluding spaces.
# - Number of times the letter i appears.

# Message = "Python is very interesting"

# print(Message.count)
# print(Message.replace(" ","") .count)
# print(Message.find("i"))

# Q4. Replace text
# Replace "Java" with "Python" and print the updated sentence.

# Sentence = "I love Java programming"

# print(Sentence.replace("Java", "Python"))

# Q5. String slicing
# # Print:
# - First 4 characters.
# - Last 4 characters.
# - Characters from index 2 to 7.
# - The complete word in reverse order.

# word = "Programming"

# words = (word[0:4])
# print(words)

# words = (word[7:11])
# print(words)

# words = (word[2:8])
# print(words)

# print(words.reversed())

# # Remove extra spaces
# Perform the following:
# - Remove spaces from both sides.
# - Remove spaces only from the left.
# - Remove spaces only from the right.
# Print all three results.

# name = "   Aditi Srivastava   "

# print(name.replace("   ", ""))
# print(name.replace("   Aditi Srivastava   ", "Aditi Srivastava   ."))
# print(name.replace("   Aditi Srivastava   ", ".   Aditi Srivastava"))

# Q7. Check whether a word exists
# Check:
# - Whether "Python" exists in the sentence.
# - Whether "Java" exists in the sentence.
# - How many times "Python" appears.

# sentence = ("Python is easy to learn and Python is powerful")

# if(sentence.count("Python")>0):
#     print("Found")
    
# else:
#     print("Not Found")

# if(sentence.count("Java")>0):
#     print("Found")
    
# else:
#     print("Not Found")

# print(sentence.count("Python"))