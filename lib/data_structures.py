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
    return [spicy_food['name'] for spicy_food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        name = spicy_food['name']
        cuisine = spicy_food['cuisine']
        heat_level = spicy_food['heat_level'] * "🌶"
        print(f'{name} ({cuisine}) | Heat Level: {heat_level}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food['cuisine'] == cuisine:
            return spicy_food

def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        if spicy_food['heat_level'] > 5:
            name = spicy_food['name']
            cuisine = spicy_food['cuisine']
            heat_level = spicy_food['heat_level'] * "🌶"
            print(f'{name} ({cuisine}) | Heat Level: {heat_level}')



def get_average_heat_level(spicy_foods):
    total_heat = sum(spicy_food['heat_level'] for spicy_food in spicy_foods)

    food_num = len(spicy_foods)

    average_level = total_heat // food_num

    return average_level

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)

    return spicy_foods
