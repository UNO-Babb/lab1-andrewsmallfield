#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("Enter a place: ")
  noun2 = input("Enter a activity: " )
  noun3 = input("Enter a place: " )
  noun4 = input("Enter a object: " )
  noun5 = input("Enter a sport: " )
  noun6 = input("Enter a food: " )
  #Print the story with the user supplied words.
  print("I went to " +noun1 +" this summer and went " +noun2 +" in the ocean. " " Then I went to the " +noun3+ " and bought a " +noun4+ ", I also played " +noun5+ " and got some " +noun6+ " at the crabshack afterwards.")

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
