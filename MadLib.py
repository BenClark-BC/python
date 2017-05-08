"""This is a Python Mad Lib. Upon execution it will prompt the user for serveral word inputs to help complete a story."""

print "Begin program! Mad Libs is running!"

name = raw_input("Enter the name of the main character: ")
adj1 = raw_input("Enter an adjective, 1 of 3 (big, loud, etc): ")
adj2 = raw_input("Enter an adjective, 2 of 3 (big, loud, etc): ")
adj3 = raw_input("Enter an adjective, 3 of 3 (big, loud, etc): ")
verb1 = raw_input("Enter a verb, 1 of 3 (run, climb, etc): ")
verb2 = raw_input("Enter a verb, 2 of 3 (run, climb, etc): ")
verb3 = raw_input("Enter a verb, 3 of 3 (run, climb, etc): ")
noun1 = raw_input("Enter a noun, 1 of 4 (dog, bike, etc): ")
noun2 = raw_input("Enter a noun, 2 of 4 (dog, bike, etc): ")
noun3 = raw_input("Enter a noun, 3 of 4 (dog, bike, etc): ")
noun4 = raw_input("Enter a noun, 4 of 4 (dog, bike, etc): ")
animal = raw_input("Enter the first animal you think of: ")
food = raw_input("Enter the last food you ate: ")
fruit = raw_input("Enter your favorite fruit: ")
number = raw_input("Enter your age plus 9: ")
superhero = raw_input("Enter the silliest Superhero you can think of: ")
country = raw_input("Enter any country name: ")
dessert = raw_input("Enter the dessert you want after dinner: ")
year = raw_input("Enter the current year plus two: ")





#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."

print STORY % (adj1, name, verb1, adj2, noun1, noun2, animal, food, verb2, noun3, fruit, adj3, name, verb3, number, name, superhero, superhero, name, country, name, dessert, name, year, noun4)