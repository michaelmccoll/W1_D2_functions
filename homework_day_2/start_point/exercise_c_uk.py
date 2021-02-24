united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
print(" ")
print("Task # 1")


# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
print(" ")
print("Task # 2")

united_kingdom.append({
  "name": "Northern Irelend",
  "population": 1811000,
  "capital": "Belfast"
  })

print(united_kingdom)

# 3. Use a loop to print the names of all the countries in the UK.
print(" ")
print("Task # 3")

for countries in united_kingdom:
  print(f'{countries["name"]}')

# 4. Use a loop to find the total population of the UK.
print(" ")
print("Task # 4")

total_pop = 0

for countries in united_kingdom:
  total_pop += countries["population"]

print(total_pop)