"""print("Hello")
name = "Fakemaker"
tall = "180"
age = "17"
age2 = 17
age3 = (age2+5)
print("My son is Caden, called "+name+". He is "+ tall+"and "+age+" years old")
print("My age is "+str(age3))"""

#line hidden



"""import random
point = 0
while point <3:
  choice = input('Enter a choice (rock, paper, scissors):')
  p_choice = ['rock','paper','scissors']
  c_choice = random.choice(p_choice)
  print('You choose',(choice), ',computer choose', (c_choice))
  if choice == c_choice:
     print('ohayo')
  if c_choice == "paper":
    if choice == "scissors":
      print("u win")
      point += 1
  if c_choice == "scissors":
    if choice == "rock":
      print("u win")
      point += 1
  if c_choice == "rock":
    if choice == "paper":
      print("u win")
      point += 1
  if c_choice == "paper":
    if choice == "rock":
      print("u lose")
  if c_choice == "scissors":
    if choice == "paper":
      print("u lose")
  if c_choice == "rock":
    if choice == "scissors":
      print("u lose")"""

#line hidden



"""from re import X


def subtract(x,y):
  minus two numbers.
  return x-y

def add(x,y):
  add two numbers together.
  return x+y

def multiply(x,y):
  multiply two numbers.
  return x*y

def divide(x,y):
  divide two numbers.
  return x/y 


while True:
  print("1.Addition\n2.Substraction\n3.Multiplication\n4.Divison")
  choice = input('Enter a choice (1, 2, 3, 4):')
  if choice in ("1","2","3","4"):
    x = float(input('Enter a number'))
    y = float(input('Enter a number'))
    if choice == "1":
      print ("add",add(x,y))
    elif choice == "2":
      print ("minus",subtract(x,y)) 
    elif choice == "3":
      print ("multiply",multiply(x,y))
    elif choice == "4":
      print ("divide",divide(x,y))"""





import random
health_points=100
gold = 50
distance = 0
total_distance = 0
obstacle_hit_damage = 15
win_distance = 1000



print("                      Subway Surfers\n")
print("Hi everyone ~ Welcome to Subway Surfers! ( ˘͈ ᵕ ˘͈♡)\n")
print("This game provides an adventure experience. Players will control a virtual character running around subway tracks, dodging randomly generated obstacles, and choosing skills to help yourself runfarther\n\nAt the beginning, u have 100💗 health points, 50💗 golds and start running from 0 meters.\n\nWhen ur health point becomes 0 then u died and game over.\nIf the total distance reach to 1000💗 meters then game over, u win \n\nIn the game, you can choose 'skills' to unlock talents, touch one obstacle will minus 15 health point, one jump need 5💗 golds\n\n\nSkills Provide (Use golds to buy)🌺🌺\nShield(20 golds🌸): After using shield, u will increase 15 health points\n\nRocket(50 golds🌸): You can fly a long distance in the air directly without encounter obstacles\n\n ")


print("Now game start! Good luck and have fun!! ( ദ്ദി ˙ᗜ˙ )\n")
print("Now u run from 0 meters and have 50 golds")
while health_points > 0 and total_distance < win_distance:
  
  hit_obstacle = random.randint(1,3)
  print("\nChoose ur action")
  print("1.Run directly\n2.Jump\n3.Skills\n4.Check ur status")
  choice = input("Choose ur action(1,2,3,4):")
  if choice == "1":
    distance = random.randint(10,50)
    gold += 15
    print("\nYou run",distance,"meters")
    print("You earn 15🌹golds")
    total_distance = total_distance + distance
    
    if hit_obstacle == 2:
      health_points -= 15
      print ("\nOh no you encounter an obstacle")
      print ("You lost 15🌹health points")
  
    
  elif choice == "2":
      distance = random.randint(40,100)
      gold -= 5
      print("\nYou jumped and ran",distance,"meters")
      print("You lost 5🌹golds")
      total_distance = total_distance + distance
      if hit_obstacle == 2:
        health_points -= 15
        print ("\nOh no you encounter an obstacle")
        print ("You lost 15🌹health points")
    
  elif choice == "3":
      print("\nSkills available:")
      print("1.😊shield(cost 20 golds)")
      print("2.😊rocket(cost 50 golds)")
      skill_choice = input("\nChoose a skill to buy (1or2):")

      
        
      if skill_choice == "1" and gold >= 20:
           gold -= 20
           health_points += 15
           print("You health points increase 15!!! You became stronger!!Σ(･o･;) ﾊｯ!")
      elif skill_choice == "1" and gold <= 20:
           print("There's no enough golds.😭")
        
     
        
      if skill_choice == "2" and gold >= 50:
            gold -= 50
            distance = random.randint(150,250)
            total_distance = total_distance + distance
            print("You used a rocktet to fly",distance,"meters!! (´⊙ω⊙`)ᵒᵐᵍᵎᵎᵎ")
            if hit_obstacle == 2:
               health_points -= 15
            print ("\nOh no you encounter an obstacle")
            print ("You lost 15🌹health points")
        
      elif skill_choice == "2" and gold <= 50:
            print("There's no enough golds.😭")
       
      
        
  if choice == "4":
    
    print ("\n🦊current health:",health_points)
    print ("🦊current golds:",gold)
    print ("🦊current total_distance:",total_distance)
  
  


if total_distance >= win_distance:
      print("\nYou have reached 1000 meters!\nCongratulations!!! You win!!!   ദ്ദി ˉ͈̀꒳ˉ͈́ )✧")
  
if health_points <= 0:
      print ("\nGame over! You ran out of health points...(,,>﹏<,,)")



