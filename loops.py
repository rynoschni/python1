title = "The Matrix Corp"
#STOP = 10
counter = 0
#while loop
# hardcode stop, change len(title) to STOP
#while counter < len(title):
 #   print(title[counter])
   #counter = counter + 1 or shorthand
  #  counter += 1
    
#while counter < len(title):
 #   if (counter % 2) == 0:
  #      print(title[counter]) #single line, add ,end = ""
   # counter += 1

while counter < len(title):
    if (counter % 2) == 0 and title[counter] != " ":
        print(title[counter])
    counter += 1