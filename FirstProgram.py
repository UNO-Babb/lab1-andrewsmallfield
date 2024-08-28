#FirstProgram.py
#Name: Andrew Smallfield
#Date: 08/28/2024
#Assignment: Lab 1

def main():
  print("First Program")
  #Say hello
  print("Hello, how are you?")
  #Ask for the user's name
  name = input("What is your name? ")
  #Use the user's name in the program.
  print("Good to meet you", name )
  #Ask the user for their age.
  Age =input("How old are you? ")
  #Tell the user what year they were born in.
  Age = int(Age)
  born=2024 - Age
  #Assume that they have not had their birthday yet this year.
  print(born) 

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
