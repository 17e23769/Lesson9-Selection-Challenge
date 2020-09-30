import time
score = 0
print ("Welcome To The Joke Game!")
time.sleep(1)
print ("Here Is The First Joke!")
time.sleep(2)
print ("\n")
print ("what is pink and fluffy?")
a = str(input())
if a == str("pink fluff"):
  print ("You Are Correct!")
  score = score + 1
  print (score)
else:
  print ("You Are Wrong")
  print (score)
time.sleep(1)
print("\n")
print("Would You Like To See The Next Joke? please type yes or no")
a = str(input())
if a == str("no"):
  print ("OK Goodbye")

if a == str("yes"):
  print("OK Here Is The Next Joke!")
  time.sleep(2)
  print("What is brown and sticky?")
  a = str(input())
  if a == str("a brown stick"):
    print ("You Are Correct!")
    score = score + 1
    print (score)
  else:
    print ("you are wrong")
    print (score)
  print ("\n")
  print("Would You Like To See The Last Joke? please type yes or no")
  a = str(input())

  if a == str("no"):
    print("OK Goodbye")
  if a == str("yes"):
    print ("OK Here Is The Last Joke!")
    print ("\n")
    time.sleep(2)
    print ("What Is Black And White And Red All Over?")
    a = str(input())
    if a == str("a newspaper"):
      print ("You Are Correct!")
      print ("\n")
      score = score + 1
      print ("this is your final score!")
      print ("\n")
      print (score)
      print ("Thank You For Playing The Joke Game!")
    else:
      print ("You Are Wrong")
      print ("\n")
      print ("this is your final score!")
      print (score)
      print ("Thank You For Playing The Joke Game!")