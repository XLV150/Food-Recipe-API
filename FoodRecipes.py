import requests

url = "https://low-carb-recipes.p.rapidapi.com/random"

headers = {
    "X-RapidAPI-Key": "Your API KEY",
    "X-RapidAPI-Host": "low-carb-recipes.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response)
print()

if response.status_code == 200:
    data = response.json()
    # print(data)
    name = data['name']
    description = data['description']
    print(type(description))
    preptime = data['prepareTime']
    cooktime = data['cookTime']
    servings = data['servings']
    servingSizes = data['servingSizes'][0]['grams']

    # General meal details
    print("Dish: ", name)
    print("Description: ", description)
    print("Meal preptime: ", preptime, "mins")
    print("Meal CookTime: ", cooktime, "mins")
    print("Servings: ", servings)
    print("Serving Sizes: ", servingSizes, "grams")
    print()

    # Ingredient counter and print func
    len1 = len(data['ingredients'])
    # print(len1)

    for i in range(len1):
        ingredients = data['ingredients'][i]['name']
        ingredientsdesc = data['ingredients'][i]['servingSize']['desc']
        print(f'Ingredient {i + 1}: ', ingredients, "| Amount: ", ingredientsdesc)
    print()

    # Steps Counter and print func
    len2 = len(data['steps'])
    # print(len2)

    for x in range(len2):
        steps = data['steps'][x]
        print(f"Step {x + 1}: ", steps)
    print()

    # Nutritional value of meal
    for item in data['nutrients']:
        nutrients_no = data['nutrients'][item]
        print('Nutrients: ', item, nutrients_no)
    