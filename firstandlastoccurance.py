s = str(input("Enter the word: "))

if s.count("f") >= 2:
  print(s.find("f"), s.rfind("f"))
elif s.find("f") == 0:
  print(s.find("f"))
else:
  print(s.find("f"))