from random import *

name = input("What are you cooking?: ")
ingredients = input("What goes in it? (use commas): ").split(", ")

change = ("apples", "asparagus", "bananas", "beans", "beef", "beets", "bell peppers", "blueberries", "broccoli",
          "brussels sprouts", "cabbage", "cane berries", "carrots", "cauliflower", "celery", "cheese", "cherries",
          "chicken", "corn", "cranberries", "cucumber", "eggplant", "eggs", "garlic", "grapes", "green beans",
          "hot peppers", "kale", "kiwi", "leeks", "lentils", "mango", "milk", "mushrooms", "oats", "onions", "oranges",
          "parsnips", "peaches", "pears", "peas", "pineapple", "pork", "potatoes", "pumpkin", "radishes", "rhubarb",
          "rice", "salmon", "spinach", "strawberries", "sweet potato", "tofu", "tomatoes", "tuna", "turkey", "turnips",
          "water", "watermelon", "flour", "squash", "yogurt")

f_name = ("Ada", "Agnes", "Alice", "Amelia", "Audra", "Audrey", "Ava", "Beatrice", "Bessie", "Blanche", "Cicely",
          "Cora", "Cordelia", "Dinah", "Dora", "Dorothea", "Dorothy", "Harriet", "Edith", "Elise", "Elsie", "Elspeth",
          "Emily", "Emmeline", "Esme", "Eva", "Evelyn", "Evie", "Flora", "Florence", "Greta", "Gretchen", "Harriet",
          "Hattie", "Irene", "Iris", "Ivy", "Lena", "Lilith", "Lillian", "Mabel", "Maisie", "Maggie", "Margaret",
          "Martha", "Mary", "Matilda", "May", "Millicent", "Millie", "Meredith", "Myrtle", "Nell", "Nellie", "Nora",
          "Olive", "Pearl", "Rosaline", "Rosalie", "Rose", "Winifred")

l_name = ('Smith', 'Jones', 'Taylor', 'Brown', 'Williams', 'Wilson', 'Johnson', 'Davies', 'Patel', 'Robinson',
          'Wright', 'Thompson', 'Evans', 'Walker', 'White', 'Roberts', 'Green', 'Hall', 'Thomas', 'Clarke', 'Jackson',
          'Wood', 'Harris', 'Edwards', 'Turner', 'Martin', 'Cooper', 'Hill', 'Ward', 'Hughes', 'Moore', 'Clark', 'King',
          'Harrison', 'Lewis', 'Baker', 'Lee', 'Allen', 'Morris', 'Khan', 'Scott', 'Watson', 'Davis', 'Parker', 'James',
          'Bennett', 'Young', 'Phillips', 'Richardson', 'Mitchell', 'Bailey', 'Carter', 'Cook', 'Singh', 'Shaw', 'Bell',
          'Collins', 'Morgan', 'Kelly', 'Begum', 'Miller', 'Cox', 'Hussain', 'Marshall', 'Simpson', 'Price', 'Anderson',
          'Adams', 'Wilkinson', 'Ali', 'Ahmed', 'Foster', 'Elli', 'Murphy', 'Chapman', 'Mason', 'Gray', 'Richards',
          'Webb', 'Griffiths', 'Hunt', 'Palmer', 'Campbell', 'Holmes', 'Mills', 'Rogers', 'Barnes', 'Knight',
          'Matthews', 'Barker', 'Powell', 'Stevens', 'Fisher', 'Butler', 'Dixon', 'Russell', 'Harvey',
          'Pearson', ' Graham')


def name_picker(b_arg):
    pick = randint(0, len(b_arg))
    return pick


print(name, "recipe\n-=-=-=-=-=-=-=-=-=-=-=-=-")
print(*ingredients, sep="\n")
print("-=-=-=-=-=-=-=-=-=-=-=-=-\n", f_name[name_picker(f_name)], l_name[name_picker(l_name)],
      "\nOh, I love this recipe, but instead of", ingredients[name_picker(ingredients)], "I used",
      change[name_picker(change)])
