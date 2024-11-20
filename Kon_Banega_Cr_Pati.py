questions = [
    ["Which language is used to create fb ?" , "Python", "JavaScript", "Java", "French", 4],
    ["Which language is used to create fb ?" , "Python", "JavaScript", "Java", "French", 4],
    ["Which language is used to create fb ?" , "Python", "JavaScript", "Java", "French", 4],
    ["Which language is used to create fb ?" , "Python", "JavaScript", "Java", "French", 4],
    ["Which language is used to create fb ?" , "Python", "JavaScript", "Java", "French", 4],
    ["Which language is used to create fb ?" , "Python", "JavaScript", "Java", "French", 4],
    ["Which language is used to create fb ?" , "Python", "JavaScript", "Java", "French", 4],
    ["Which language is used to create fb ?" , "Python", "JavaScript", "Java", "French", 4],
    ["Which language is used to create fb ?" , "Python", "JavaScript", "Java", "French", 4],
    ["Which language is used to create fb ?" , "Python", "JavaScript", "Java", "French", 4],
    ["Which language is used to create fb ?" , "Python", "JavaScript", "Java", "French", 4],
    ["Which language is used to create fb ?" , "Python", "JavaScript", "Java", "French", 4],
    ["Which language is used to create fb ?" , "Python", "JavaScript", "Java", "French", 4]
    ]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 
160000, 320000, 640000, 1200000, 2400000]

money = 0

for i in range(0, len(questions)):
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"Q{i+1}. {question[0]}")
  print(f"a. {question[1]}              b. {question[2]}")
  print(f"c. {question[3]}              d. {question[4]}")
  reply = int(input("Enter your answer (1-4) or 0 to quit."))
  if(reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, You hava won Rs. {levels[i]}")
    if(i == 4):
        money = 10000
    elif(1 == 7):
        money = 320000
    elif(1 == 12):
        money = 1000000
  else:
    print("Wrong answer!")
    break

print(f"Your take Home Money is : {money}")    