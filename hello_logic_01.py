
# This program takes input from the user
# and does something different depending on the value!

users_favorite_food = input("What is your favorite food? ")

if len(users_favorite_food) < 1:
  print("That wasn't a real answer!")

elif "ice" in users_favorite_food.lower() and "cream" in users_favorite_food.lower():
  # If the user said they like "ice cream" or "chocolate ice cream with strawberries"
  # this branch will be run.
  # Notice how we can be vague to catch many different ways the user
  # might say they like ice cream.
  print("I like ice cream too!")

elif "pie " in users_favorite_food.lower() or " pie" in users_favorite_food.lower():
  print("Pie is my favorite food!")

else:
  print("I have never heard of "+users_favorite_food+" before, but I bet it is good!")

