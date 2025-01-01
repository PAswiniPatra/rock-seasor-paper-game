import random 

my_list = ["rock","paper","sejer"]
rendom_str = random.choice(my_list)
print(rendom_str)
user = input("enter the move :")

if user == rendom_str :
      print("match tie") 
elif rendom_str == "sejer" and user == "paper" :
          print("computer win")        
elif rendom_str == "rock" and user == "paper" :
          print("user win")    
elif rendom_str == "sejer" and user == "rock" :
          print("user win")
elif rendom_str == "paper" and user == "sejer" :
          print("user win")        
elif rendom_str == "paper" and user == "rock" :
          print("computer win")    
elif rendom_str == "rock" and user == "sejer" :
          print("computer win")

                                                  