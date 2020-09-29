import time
score = 0
print ("Welcome To The Joke Game!")
time.sleep(2)
print ("Here Is The First Joke!")
time.sleep(3)
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
time.sleep(3)
print("\n")
print("Would You Like To See The Next Joke? please type yes or no")
a = str(input())
if a == str("no"):
  print ("OK Goodbye")

if a == str("yes"):
  print("OK Here Is The Next Joke!")
  time.sleep(3)
  print("What is brown and sticky?")
  a = str(input())
  if a == str("a brown stick"):
    print ("You Are Correct!")
    score = score + 1
    print (score)
  else:
    print ("you are wrong")
    print (score)