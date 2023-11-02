def breakFunction():
    for i in range(1, 11):
    
        if i == 5:
            break
    print(i)

def main():
    breakFunction()

main()

Greetings="ABCDEF"
a=len(Greetings)
print(a)

print("This\tis a string\twith multiple\ttabs")

# Hard-coded password, ChatGPT
correct_password = "P@$$W0RD"

while True:
    user_input = input("Type your password: ")
    
    if user_input == correct_password:
        print("Your password is correct.")
        break
    else:
        print("Your password is incorrect.")
