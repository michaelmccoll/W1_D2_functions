users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print("Task # 1")

print(users["Jonathan"]["twitter"])

# 2. Get Erik's hometown
print(" ")
print("Task # 2")

print(users["Erik"]["home_town"])

# 3. Get the array of Erik's lottery numbers
print(" ")
print("Task # 3")

print(users["Erik"]["lottery_numbers"])

# 4. Get the species of Avril's pet Monty
print(" ")
print("Task # 4")

avril_pet_species = users["Avril"]["pets"]
print(avril_pet_species)

# 5. Get the smallest of Erik's lottery numbers
print(" ")
print("Task # 5")

min_lottery_num = min(users["Erik"]["lottery_numbers"])
print(min_lottery_num)

# 6. Return an array of Avril's lottery numbers that are even
print(" ")
print("Task # 6")

for num in users["Avril"]["lottery_numbers"]:
  if num % 2 == 0:
    print(num)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
print(" ")
print("Task # 7")

users["Erik"]["lottery_numbers"].append("7")
print(users["Erik"]["lottery_numbers"])

# 8. Change Erik's hometown to Edinburgh
print(" ")
print("Task # 8")

users["Erik"]["home_town"]="Edinburgh"
print(users["Erik"]["home_town"])

# 9. Add a pet dog to Erik called "Fluffy"
print(" ")
print("Task # 9")

users["Erik"]["pets"].append({"name":"Fluffy"})

print(users["Erik"]["pets"])

# 10. Add another person to the users dictionary
print(" ")
print("Task # 9")

users.update({"John":None})

print(users.keys())
