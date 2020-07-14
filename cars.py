languages = { 'english', 'mandarin chinese', 'spanish', 'english', 'spanish', 'portugese' }
print(languages)
languages.add("hindi")
print(languages)
for language in languages:
    print(language)
instructors = {"Joe", "Madi", "Bryan"}
# Check for item in a collection (You can do this with lists, dictionaries, and tuples as well!)
if "Joe" in instructors:
    print("Yes, Joe is in this collection")

showroom = set()
showroom = {"Mini", "MDX", "Altima", "Accord"}
print(showroom)
print(len(showroom))

new_cars = {"Camry", "LX5"}
showroom.update(new_cars)
print("new cars:", showroom)
showroom.discard("Camry")
print(showroom)

junkyard = {"Mustang", "Accord", "BMW", "Porche", "MDX"}
garage = showroom.intersection(junkyard)
print("garage:", garage)
showroom = showroom.union(junkyard)
print("bigger", showroom)