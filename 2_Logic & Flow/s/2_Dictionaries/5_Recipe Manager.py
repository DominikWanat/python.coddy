# Write code here
recipe_book = {}
recipe_book["Pancakes"] = ["flour", "milk", "eggs", "sugar"]
recipe_book["Salad"] = ["lettuce", "tomato", "cucumber", "olive oil"]

#def create_recipe_book(recipe_book,recipes,ingredients):

print(recipe_book["Pancakes"])

recipe_book["Smoothie"] = ["banana", "milk", "honey"]

recipe_book["Smoothie"] += ["blueberries"]

print(recipe_book)

########################################################################

# Step 1: Create the Recipe Book
recipe_book = {
    "Pancakes": ["flour", "milk", "eggs", "sugar"],
    "Salad": ["lettuce", "tomato", "cucumber", "olive oil"]
}

# Step 2: Access Ingredients for "Pancakes"
print(recipe_book["Pancakes"])

# Step 3: Add a New Recipe
recipe_book["Smoothie"] = ["banana", "milk", "honey"]

# Step 4: Modify the "Smoothie" Recipe
recipe_book["Smoothie"].append("blueberries")

# Step 5: Print All Recipes
print(recipe_book)