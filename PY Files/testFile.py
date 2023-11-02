"""
file_path = "D:\\Personal\\Yaseen\\RIT (Rochester Institute of Technology)\\Software Developement\\PY Files\\testFile.txt"

def wordsearch():
    with open(file_path, 'r') as my_file:
        lines = my_file.readlines()
        for line_number, line in enumerate(lines, start=1):  # Use enumerate to get line numbers
            if 'human' in line:
                print(f'String "human" found on line {line_number}: {line.strip()}')

# Call the function to search for the word "human"
wordsearch()
"""

# Activity 5.1.5:-

def longest_word():
    """Open the file for reading"""
    with open("D:\\Personal\\Yaseen\\RIT (Rochester Institute of Technology)\\Software Developement\\PY Files\\testFile.txt", "r") as f:
        """Read all lines into a list"""
        lines = f.readlines()
        
        """Iterate over the lines"""
        for line in lines:
            """Split the line into words"""
            words = line.split()
            
            """Find the longest word in the line"""
            longest = max(words, key=len)
            
            """Print the longest word in each line"""
            print(f"Longest word in line: {line.strip()} is: {longest}")

"""Call the function"""
longest_word()  