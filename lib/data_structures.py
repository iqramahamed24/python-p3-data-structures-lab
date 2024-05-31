spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    for food in spicy_foods:
        print(food["name"])

get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
   spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
   return spiciest_foods
get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food[heat_level]
        heat_emojis = "🌶" * heat_level
        print(f"{name} ({cuisine}) \ Heat Level: {heat_emojis}")
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get('cuisine') == cuisine:
            return food
    return None
print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))


def print_spiciest_foods(spicy_foods):
    print("Spiciest Foods:")
    for food in spicy_foods:
        if food.get('heat_level', 0) > 5:
            print(f"Name: {food['name']}, Cuisine: {food['cuisine']}, Heat Level: {food['heat_level']}")
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    
    total_heat = 0
    for food in spicy_foods:
        total_heat += food.get('heat_level', 0)
    
    average_heat = total_heat // len(spicy_foods)
    
    return average_heat

print(get_average_heat_level(spicy_foods))


def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods
new_spicy_food = {
    'name': 'Griot',
    'cuisine' : 'Haitian',
    'heat_level' : 10,
}
updated_spicy_foods = create_spicy_food(spicy_foods, new_spicy_food)
print(updated_spicy_foods)

