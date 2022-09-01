Red = "\033[0;31m"
Blue = "\033[0;34m"


while True:
  


  def qcolor(question):
    return input(Red + question + Blue)

  beginning = qcolor("Hello, are you ready for the quiz?")

  if beginning == 'yes' or beginning == 'Yes':
    print(Red + "Let's begin the quiz!")

  print("")
 
  
  Answer1 = qcolor("What is the name of the planet you live on? ")
  
  if Answer1 == 'earth' or Answer1 == 'Earth':
    print(Red + "Correct answer!")
  else:
    print(Red + "wrong answer! The correct answer is Earth" )

  print("")
    
  Answer2 = qcolor("How many planets are there in our solar system? ")
 
  if Answer2 == '8':
    print(Red + "Correct answer!")
  else:
    print(Red + "wrong answer! The correct answer is 8")

  print("")

  Answer3 = qcolor("What planet is in front of Earth? ")
  
  if Answer3 == 'Venus' or Answer3 == 'venus':
    print(Red + "Correct answer!")
  else:
    print(Red + "wrong answer! The correct answer is Venus")

  print("")

  Answer4 = qcolor("How many named moons does Jupiter have? ")
 
  if Answer4 == '53':
    print(Red + "Correct answer!")
  else:
    print(Red + "wrong answer! The correct answer is 53")

  print("") 

  Answer5 = qcolor("How old is the Earth? ")
 
  if Answer5 == '4.543 billion years':
    print(Red + "Correct answer!")
  else:
    print(Red + "wrong answer! The correct answer is 4.543 billion years")

  print("") 

  Answer6 = qcolor("Can a star turn into a planet? ")
 
  if Answer6 == 'Yes' or Answer6 == 'yes':
    print(Red + "Correct answer!")
  else:
    print(Red + "wrong answer! The correct answer is yes")

  print("") 

  Answer7 = qcolor("What kind of star turns into a planet? ")
 
  if Answer7 == 'A brown dwarf' or Answer7 == 'a brown dwarf':
    print(Red + "Correct answer!")
  else:
    print(Red + "wrong answer! The correct answer is a brown dwarf")

  print("")  

  Answer8 = qcolor("How many failed stars are there in our solar system? ")
 
  if Answer8 == '2':
    print(Red + "Correct answer!")
  else:
    print(Red + "wrong answer! The correct answer is 2")

  print("") 

  Answer9 = qcolor("What are the two failed stars in our solar system? ")
 
  if Answer9 == 'Saturn and Jupiter' or Answer9 == 'saturn and jupiter' or Answer9 == ' Jupiter and Saturn' or Answer9 == 'jupiter and saturn':
    print(Red + "Correct answer!")
  else:
    print(Red + "wrong answer! The correct answer is Saturn and Jupiter")

  print("") 

  Answer10 = qcolor("Is Pluto a dwarf planet? ")
 
  if Answer10 == 'Yes' or Answer10 == 'yes':
    print(Red + "Correct answer!")
  else:
    print(Red + "wrong answer! The correct answer is yes")

  print("")

  end = qcolor("Did you enjoy this quiz?")

  if end == 'yes':
    print(Red + "Have a great day!")

  else:
    print(Red + "Have a good day!")

  print("")
  print("")
  break

